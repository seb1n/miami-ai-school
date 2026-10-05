"""Rebuild a clean classroom ZIP; does not include secrets, local runs or transient QA."""
from pathlib import Path
import hashlib,json,zipfile
root=Path(__file__).resolve().parent;out=root.parent/'Source_to_Studio_Starter.zip'
exclude_dirs={'__pycache__','runs','.git','.venv','node_modules'}
exclude_names={'MANIFEST.json','browser-smoke-log.txt','ui-state-log.txt'}
files=[]
for p in root.rglob('*'):
 if not p.is_file():continue
 rel=p.relative_to(root)
 if any(x in exclude_dirs for x in rel.parts) or p.name in exclude_names or p.name.startswith('.env') or p.suffix=='.pyc':continue
 if rel.parts[0]=='evidence' and (p.suffix in {'.png','.zip'}):continue
 files.append(p)
manifest={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
(root/'MANIFEST.json').write_text(json.dumps(manifest,indent=2));files.append(root/'MANIFEST.json')
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(files):z.write(p,'starter/'+str(p.relative_to(root)))
print(out);print(out.stat().st_size,'bytes;',len(files),'files');print('SHA256',hashlib.sha256(out.read_bytes()).hexdigest())
