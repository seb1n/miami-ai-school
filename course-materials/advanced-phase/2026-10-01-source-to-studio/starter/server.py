#!/usr/bin/env python3
"""Local classroom app. Python 3.10+. No third-party Python dependencies."""
import argparse, io, json, mimetypes, os, re, secrets, shutil, threading, zipfile
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse
from core import ROOT, KINDS, Store, WorkflowError, digest, load_json, now, validate_source
from render_video import render
from agents_adapter import generate

LOCK=threading.RLock();STORE=Store();CSRF=secrets.token_urlsafe(24)

def run_action(data):
    action=data.get('action');rid=data.get('id');version=data.get('version')
    with LOCK:
        if action=='create':
            mode=data.get('mode','replay');scenario=data.get('scenario','good');source=load_json('source_pack.json')
            if mode=='live':
                if data.get('acknowledge_paid') is not True:raise WorkflowError('Confirm this live run may incur OpenAI charges')
                result=generate(source,data.get('revision_note',''))
                artifacts=result.pop('artifacts');return STORE.create(source,artifacts,'live','live',result)
            if mode!='replay' or scenario not in ('good','bad'):raise WorkflowError('Unknown replay scenario')
            return STORE.create(source,load_json(scenario+'.json'),'replay',scenario,{'origin':'human-authored synthetic fixture; no model called','live':False})
        if action=='revise':return STORE.revise(rid,version,data['artifacts'],data.get('source'))
        if action=='rerun_fixed':
            run=STORE.get(rid);STORE.check_version(run,version)
            if run['mode']!='replay':raise WorkflowError('Fixture repair is for replay only. Start a new explicit live run for model revision')
            if run['source_hash']!=digest(load_json('source_pack.json')):raise WorkflowError('Edited source differs from the replay fixture. Restore source or revise content manually; replay cannot regenerate new facts')
            return STORE.revise(rid,version,load_json('good.json'))
        if action=='review':return STORE.review(rid,version,data.get('kind'),data.get('decision'),data.get('note',''))
        if action=='evaluate':return STORE.evaluate(rid,version)
        if action=='sample_video':
            run=STORE.get(rid);STORE.check_version(run,version)
            if digest(run['artifacts']['video'])!=digest(load_json('good.json')['video']) or run['source_hash']!=digest(load_json('source_pack.json')):
                raise WorkflowError('Included MP4 matches only the original fixture source and video script; render edited content instead')
            sample=ROOT/'media'/'sample.mp4'
            if not sample.exists():raise WorkflowError('Included sample MP4 missing')
            output=STORE.directory/f'{rid}-v{version}.mp4';shutil.copyfile(sample,output)
            result=json.loads((ROOT/'media'/'sample_probe.json').read_text())
            result.update(version=version,video_hash=digest(run['artifacts']['video']),source_hash=run['source_hash'],filename=output.name,at=now(),renderer='included synthetic fixture MP4; not rerendered')
            run['render']=result;run['reviews'].pop('video',None);run['evaluations']=None
            run['history'].append({'at':now(),'event':'matching_fixture_mp4_loaded_review_reset','version':version})
            return STORE.save(run)
        if action=='render':
            run=STORE.get(rid);STORE.check_version(run,version)
            output=STORE.directory / f'{rid}-v{version}.mp4'
            result=render(run['artifacts']['video'],output)
            result.update(version=version,video_hash=digest(run['artifacts']['video']),source_hash=run['source_hash'],filename=output.name,at=now())
            run['render']=result;run['evaluations']=None
            # Rendering may change perceived quality: require fresh video approval after playing the actual MP4.
            run['reviews'].pop('video',None)
            run['history'].append({'at':now(),'event':'video_rendered_review_reset','version':version})
            return STORE.save(run)
        raise WorkflowError('Unknown action')

def export_bytes(run):
    out=io.BytesIO()
    with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
        z.writestr('run.json',json.dumps(run,indent=2,ensure_ascii=False))
        z.writestr('source_pack.json',json.dumps(run['source'],indent=2,ensure_ascii=False))
        z.writestr('artifacts.json',json.dumps(run['artifacts'],indent=2,ensure_ascii=False))
        for k in ('newsletter','linkedin','x'):z.writestr(k+'.txt',run['artifacts'][k].get('title','')+'\n\n'+run['artifacts'][k]['body'])
        z.writestr('video_script.json',json.dumps(run['artifacts']['video'],indent=2,ensure_ascii=False))
        z.writestr('REVIEW-STATUS.txt',f"SYNTHETIC CLASSROOM DRAFT | mode={run['mode']} | version={run['version']}\nNot published. Review decisions, scope and evaluation results are in run.json.\nA script is not a rendered MP4. Only video.mp4, if present, is a finished video.\n")
        r=run.get('render')
        if r and r['version']==run['version'] and r['video_hash']==digest(run['artifacts']['video']):
            path=STORE.directory/r['filename']
            if path.exists():z.write(path,'video.mp4')
    return out.getvalue()

class Handler(BaseHTTPRequestHandler):
    def log_message(self,*args):pass  # Do not log request content or secrets.
    def valid_host(self):
        return self.headers.get('Host') in (f'127.0.0.1:{self.server.server_port}',f'localhost:{self.server.server_port}')
    def send(self,body,status=200,ctype='application/json',download=None):
        if not isinstance(body,bytes):body=json.dumps(body,ensure_ascii=False).encode()
        self.send_response(status);self.send_header('Content-Type',ctype);self.send_header('Content-Length',str(len(body)));self.send_header('Cache-Control','no-store');self.send_header('X-Content-Type-Options','nosniff');self.send_header('Content-Security-Policy',"default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; media-src 'self'; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'")
        if download:self.send_header('Content-Disposition','attachment; filename="'+download+'"')
        self.end_headers();self.wfile.write(body)
    def do_GET(self):
        if not self.valid_host():return self.send({'error':'Localhost access only'},403)
        path=urlparse(self.path).path
        try:
            if path=='/api/config':return self.send({'csrf':CSRF,'default_mode':'replay','live_enabled':os.environ.get('ENABLE_LIVE')=='1' and bool(os.environ.get('OPENAI_API_KEY')),'ffmpeg_available':bool(shutil.which('ffmpeg') and shutil.which('ffprobe')),'source':load_json('source_pack.json'),'runs':[{'id':r['id'],'version':r['version'],'scenario':r['scenario'],'mode':r['mode']} for r in STORE.list()]})
            if path.startswith('/api/run/'):return self.send(STORE.get(path.rsplit('/',1)[-1]))
            if path.startswith('/export/'):
                run=STORE.get(path.rsplit('/',1)[-1]);return self.send(export_bytes(run),ctype='application/zip',download=f"content-{run['id']}-v{run['version']}.zip")
            if re.fullmatch(r'/media/[a-f0-9]{12}-v\d+\.mp4',path):
                p=STORE.directory/path.rsplit('/',1)[-1]
            elif path=='/sample.mp4':p=ROOT/'media'/'sample.mp4'
            elif path in ('/','/app.js','/style.css'):p=ROOT/'web'/('index.html' if path=='/' else path[1:])
            else:return self.send({'error':'Not found'},404)
            if not p.exists():return self.send({'error':'File not available'},404)
            return self.send(p.read_bytes(),ctype=mimetypes.guess_type(str(p))[0] or 'application/octet-stream')
        except WorkflowError as e:return self.send({'error':str(e)},400)
        except Exception:return self.send({'error':'Read failed; check local files'},500)
    def do_POST(self):
        if not self.valid_host():return self.send({'error':'Localhost access only'},403)
        expected={f'http://127.0.0.1:{self.server.server_port}',f'http://localhost:{self.server.server_port}'}
        if self.headers.get('Origin') not in expected or self.headers.get('X-Classroom-Token')!=CSRF:return self.send({'error':'Reload the classroom app before acting'},403)
        if self.path!='/api/action':return self.send({'error':'Not found'},404)
        try:
            length=int(self.headers.get('Content-Length','0'))
            if not 0<length<=100000:raise WorkflowError('Request must be under 100 KB')
            data=json.loads(self.rfile.read(length))
            if not isinstance(data,dict):raise WorkflowError('JSON object required')
            return self.send(run_action(data))
        except (WorkflowError,json.JSONDecodeError,KeyError,TypeError,ValueError) as e:return self.send({'error':str(e)},400)
        except Exception:return self.send({'error':'Operation failed. No success is recorded; inspect local setup and retry only after checking state'},500)

def main():
    global STORE
    p=argparse.ArgumentParser();p.add_argument('--port',type=int,default=8765);p.add_argument('--runs',default=str(ROOT/'runs'));args=p.parse_args()
    STORE=Store(args.runs);httpd=ThreadingHTTPServer(('127.0.0.1',args.port),Handler)
    print(f'Classroom app: http://127.0.0.1:{httpd.server_port} | REPLAY is default. Ctrl+C to stop.',flush=True)
    httpd.serve_forever()
if __name__=='__main__':main()
