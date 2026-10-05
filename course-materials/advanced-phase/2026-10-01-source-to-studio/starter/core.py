"""Classroom workflow and deterministic checks. No network, publishing or secret handling."""
from __future__ import annotations
import copy, hashlib, json, math, re, uuid
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
KINDS = ('newsletter', 'linkedin', 'x', 'video')

def now(): return datetime.now(timezone.utc).isoformat()
def digest(obj): return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
def load_json(name): return json.loads((ROOT / 'fixtures' / name).read_text(encoding='utf-8'))
def words(s): return len(re.findall(r"\b[\w]+(?:['’-][\w]+)*\b", s))

class WorkflowError(ValueError): pass

def validate_source(source):
    if not isinstance(source, dict) or not isinstance(source.get('id'), str) or not isinstance(source.get('title'), str):
        raise WorkflowError('Source pack must have id, title and source_facts')
    facts = source.get('source_facts')
    if not isinstance(facts, list) or not 1 <= len(facts) <= 50: raise WorkflowError('Supply 1–50 source facts')
    ids = []
    for f in facts:
        if not isinstance(f, dict) or any(not isinstance(f.get(k), str) or not f[k].strip() for k in ('id','text','source')):
            raise WorkflowError('Every source fact needs id, text and source')
        if len(f['text']) > 3000: raise WorkflowError('Source fact too long')
        ids.append(f['id'])
    if len(set(ids)) != len(ids): raise WorkflowError('Duplicate source fact IDs')
    c = source.get('constraints', {})
    for key in ('newsletter_max_words','linkedin_max_words','x_max_chars','video_seconds'):
        if type(c.get(key)) not in (int,float) or not math.isfinite(c[key]) or c[key] <= 0: raise WorkflowError('Missing or invalid constraint: ' + key)
    if len(json.dumps(source)) > 50000: raise WorkflowError('Source pack too large')
    return source

def validate_artifacts(artifacts):
    if not isinstance(artifacts, dict) or set(artifacts) != set(KINDS): raise WorkflowError('Need exactly newsletter, linkedin, x and video')
    for kind in KINDS:
        a = artifacts[kind]
        if not isinstance(a, dict): raise WorkflowError(kind + ' must be an object')
        if kind != 'video':
            if not isinstance(a.get('body'), str) or not a['body'].strip() or len(a['body']) > 15000: raise WorkflowError(kind + ' body must be 1–15000 characters')
            if not isinstance(a.get('citations'), list) or not all(isinstance(c,str) for c in a['citations']): raise WorkflowError(kind + ' needs citation IDs')
        if kind in ('newsletter','video') and (not isinstance(a.get('title'), str) or not 1 <= len(a['title']) <= 160): raise WorkflowError(kind + ' title required, max 160 chars')
    scenes = artifacts['video'].get('scenes')
    if not isinstance(scenes,list) or not 1 <= len(scenes) <= 8: raise WorkflowError('Video needs 1–8 scenes')
    for s in scenes:
        if not isinstance(s,dict) or not isinstance(s.get('text'),str) or not 1 <= len(s['text']) <= 280: raise WorkflowError('Each scene needs 1–280 text characters')
        if type(s.get('duration_seconds')) not in (int,float) or not math.isfinite(s['duration_seconds']) or not 1 <= s['duration_seconds'] <= 20: raise WorkflowError('Scene duration must be 1–20 seconds')
        if not isinstance(s.get('citations'),list) or not all(isinstance(c,str) for c in s['citations']): raise WorkflowError('Scene needs citation IDs')
    if sum(s['duration_seconds'] for s in scenes) > 60: raise WorkflowError('Video max 60 seconds')
    return artifacts

def artifact_schema():
    citations={'type':'array','items':{'type':'string'}}
    def obj(props): return {'type':'object','properties':props,'required':list(props),'additionalProperties':False}
    string={'type':'string'}
    body=obj({'body':string,'citations':citations})
    return obj({'newsletter':obj({'title':string,'body':string,'citations':citations}), 'linkedin':body, 'x':body, 'video':obj({'title':string,'scenes':{'type':'array','items':obj({'text':string,'duration_seconds':{'type':'number'},'citations':citations})}})})

class Store:
    def __init__(self, directory=None):
        self.directory = Path(directory or ROOT / 'runs'); self.directory.mkdir(parents=True, exist_ok=True)
    def save(self, run):
        p=self.directory / (run['id']+'.json'); tmp=p.with_suffix('.tmp')
        tmp.write_text(json.dumps(run, indent=2, ensure_ascii=False),encoding='utf-8'); tmp.replace(p); return copy.deepcopy(run)
    def get(self, rid):
        if not re.fullmatch(r'[a-f0-9]{12}',rid or ''): raise WorkflowError('Invalid run ID')
        p=self.directory/(rid+'.json')
        if not p.exists(): raise WorkflowError('Run not found')
        return json.loads(p.read_text(encoding='utf-8'))
    def list(self):
        return [json.loads(p.read_text(encoding='utf-8')) for p in sorted(self.directory.glob('*.json'),key=lambda p:p.stat().st_mtime,reverse=True)][:50]
    def create(self,source,artifacts,mode='replay',scenario='good',metadata=None):
        validate_source(source);validate_artifacts(artifacts)
        run={'id':uuid.uuid4().hex[:12],'created_at':now(),'mode':mode,'scenario':scenario,'synthetic':True,'version':1,'source':copy.deepcopy(source),'source_hash':digest(source),'artifacts':copy.deepcopy(artifacts),'artifact_hash':digest(artifacts),'reviews':{},'evaluations':None,'render':None,'history':[],'metadata':metadata or {}}
        run['history'].append({'at':now(),'event':'draft_created','version':1,'mode':mode})
        return self.save(run)
    def check_version(self,run,version):
        if type(version) is not int or version != run['version']: raise WorkflowError('Stale version. Reload before acting; earlier approval does not cover new content')
    def revise(self,rid,version,artifacts,source=None):
        run=self.get(rid);self.check_version(run,version);validate_artifacts(artifacts)
        if source is not None: validate_source(source)
        run['history'].append({'at':now(),'event':'version_archived','version':run['version'],'source':run['source'],'source_hash':run['source_hash'],'artifacts':run['artifacts'],'artifact_hash':run['artifact_hash'],'reviews':run['reviews'],'evaluations':run['evaluations'],'render':run['render']})
        run.update(version=run['version']+1,artifacts=copy.deepcopy(artifacts),artifact_hash=digest(artifacts),reviews={},evaluations=None,render=None)
        if source is not None: run.update(source=copy.deepcopy(source),source_hash=digest(source))
        run['history'].append({'at':now(),'event':'revision_created_approvals_reset','version':run['version']})
        return self.save(run)
    def review(self,rid,version,kind,decision,note=''):
        run=self.get(rid);self.check_version(run,version)
        if kind not in KINDS or decision not in ('approved','changes_requested'): raise WorkflowError('Invalid review')
        if not isinstance(note,str) or len(note)>1000: raise WorkflowError('Review note must be under 1000 characters')
        if kind=='video' and decision=='approved':
            r=run.get('render') or {}
            if r.get('version')!=version or r.get('video_hash')!=digest(run['artifacts']['video']) or r.get('source_hash')!=run['source_hash'] or not (self.directory/r.get('filename','missing')).is_file():
                raise WorkflowError('Render and play the current MP4 before approving video; a script alone is not a finished video')
        run['reviews'][kind]={'decision':decision,'version':version,'source_hash':run['source_hash'],'artifact_hash':digest(run['artifacts'][kind]),'scope':'classroom draft only; no publication permission','note':note,'at':now()}
        run['evaluations']=None
        run['history'].append({'at':now(),'event':'human_review','kind':kind,'decision':decision,'version':version})
        return self.save(run)
    def evaluate(self,rid,version):
        run=self.get(rid);self.check_version(run,version)
        if not all(k in run['reviews'] for k in KINDS): raise WorkflowError('Review all four artifacts first. Approve or request changes before formal evaluation')
        run['evaluations']=evaluate(run)
        run['history'].append({'at':now(),'event':'formal_evaluation','version':version,'machine_checks_passed':run['evaluations']['machine_checks_passed']})
        return self.save(run)

def evaluate(run):
    """Heuristics + exact rules for this synthetic fixture. Never a truth oracle."""
    a,s=run['artifacts'],run['source'];c=s['constraints'];facts={f['id']:f['text'] for f in s['source_facts']};checks=[]
    def check(cid,passed,detail):checks.append({'id':cid,'passed':bool(passed),'detail':detail})
    texts={k:(v.get('title','')+'\n'+v.get('body','')).strip() if k!='video' else v['title']+'\n'+'\n'.join(x['text'] for x in v['scenes']) for k,v in a.items()}
    for k in KINDS:
        citations=a[k].get('citations',[]) if k!='video' else [c for scene in a[k]['scenes'] for c in scene['citations']]
        check(k+'_citation_ids',bool(citations) and all(i in facts for i in citations),'Citation IDs must exist; a valid ID alone does not prove the claim')
        check(k+'_synthetic_label','synthetic' in texts[k].lower(),'Visible synthetic label is required')
        check(k+'_cta','Read the practice newsletter.' in texts[k],'Exact classroom CTA required')
        r=run['reviews'].get(k,{})
        check(k+'_review_current',r.get('version')==run['version'] and r.get('source_hash')==run['source_hash'] and r.get('artifact_hash')==digest(a[k]),'Editorial decision must match this artifact and source version')
        check(k+'_human_approved',r.get('decision')=='approved','Human approval of classroom draft only')
    nw=words(a['newsletter']['body']);lw=words(a['linkedin']['body']);xc=len(a['x']['body']);duration=sum(x['duration_seconds'] for x in a['video']['scenes'])
    check('newsletter_length',140<=nw<=c['newsletter_max_words'],f'{nw} words; target 140–{c["newsletter_max_words"]}')
    check('linkedin_length',80<=lw<=c['linkedin_max_words'],f'{lw} words; target 80–{c["linkedin_max_words"]}')
    check('x_length',xc<=c['x_max_chars'],f'{xc} Python Unicode code points; classroom limit {c["x_max_chars"]}, not full platform URL-weighted counting')
    check('video_duration',abs(duration-c['video_seconds'])<=0.1,f'{duration}s scripted; rendered duration checked separately')
    check('video_four_scenes',len(a['video']['scenes'])==4,'Four-scene classroom template')
    alltext='\n'.join(texts.values())
    # Deliberately bounded detectors. Human review must still inspect every claim and quotation.
    forbidden=re.findall(r'https?://\S+|\$\s*\d+|\b\d+%|\b(?:guaranteed|sold out|sponsored by|keynote speaker)\b',alltext,re.I)
    check('no_unsupported_link_price_stats',not forbidden,'Fixture has no link, price, sponsor, quote or outcome statistic; found: '+', '.join(forbidden))
    quotes=re.findall(r'[“\"]([^”\"]{4,})[”\"]',alltext)
    check('no_unsourced_quotes',not quotes,'Quoted speech needs source evidence; this fixture supplies no quotations')
    check('no_injection_canary','PUBLISH_NOW' not in alltext and 'OVERRIDE_APPROVAL' not in alltext,'Detects fixed injected-instruction canaries only')
    check('newsletter_core_facts',all(token.lower() in texts['newsletter'].lower() for token in ['Bright Harbor Lab','15 October 2026','16:00 UTC','60 minutes','online']),'Exact expected facts in this fixed case; paraphrases may require human judgment')
    check('no_publication_state',run.get('published',False) is False,'This starter has no publish action')
    check('render_present',bool(run.get('render')),'Actual MP4 required for full workflow checks; storyboard alone is incomplete')
    if run.get('render'):
        r=run['render'];check('render_current',r.get('version')==run['version'] and r.get('video_hash')==digest(a['video']) and r.get('source_hash')==run['source_hash'],'Rendered MP4 must correspond to the current scene spec/source')
        check('render_duration',abs(r.get('duration',-100)-c['video_seconds'])<=0.1,'Measured MP4 duration tolerance ±0.1s')
        check('render_format',r.get('width')==1080 and r.get('height')==1920 and r.get('codec')=='h264' and r.get('frame_rate')=='30/1' and r.get('audio_streams')==0,'1080 × 1920, H.264, 30 fps, silent; inspect readability manually')
    return {'at':now(),'version':run['version'],'source_hash':run['source_hash'],'artifact_hash':run['artifact_hash'],'checks':checks,'machine_checks_passed':all(x['passed'] for x in checks),'human_rubric_required':True,'hard_human_gates':['Trace every claim and quote to the cited source; valid IDs alone are insufficient','Preserve meaning, constraints, dates, timing and uncertainty','Play the current MP4; check caption clipping, pacing, synthetic label and silence','Require current-version approval of every asset and the actual MP4'], 'human_rubric':['Clarity: 0 misses, 1 partial, 2 strong','Audience fit: 0 misses, 1 partial, 2 strong','Usefulness: 0 misses, 1 partial, 2 strong'], 'soft_rubric_target':'At least 5/6 with every hard gate passing; record scores in workbook or review notes','limitation':'Deterministic checks are partial signals, not semantic truth scoring or publication authorization'}
