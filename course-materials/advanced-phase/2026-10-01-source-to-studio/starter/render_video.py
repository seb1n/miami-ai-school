"""Fixed local FFmpeg template, captioned silent H.264 MP4. No model or paid service."""
import json, shutil, subprocess, tempfile, textwrap
from pathlib import Path
from core import WorkflowError, validate_artifacts
ROOT=Path(__file__).resolve().parent

def render(video, output, ffmpeg='ffmpeg', ffprobe='ffprobe'):
    if not shutil.which(ffmpeg) or not shutil.which(ffprobe):
        raise WorkflowError('Rendering needs FFmpeg + ffprobe. Use the included sample MP4 or ask Codex to install FFmpeg from its official source with your approval')
    output=Path(output).resolve();output.parent.mkdir(parents=True,exist_ok=True)
    font=ROOT/'media'/'DejaVuSans.ttf'
    if not font.exists(): raise WorkflowError('Bundled font missing')
    with tempfile.TemporaryDirectory(prefix='content-video-') as tmp:
        td=Path(tmp);shutil.copyfile(font,td/'font.ttf')
        # Content is written to text files, never inserted in shell commands or filter expressions.
        scenes=video['scenes'];parts=[]
        for i,scene in enumerate(scenes):
            lines=[line for paragraph in scene['text'].splitlines() for line in (textwrap.wrap(paragraph,width=24,break_long_words=True) or [''])]
            if len(lines)>8: raise WorkflowError('Scene too dense for readable captions. Shorten it to eight wrapped lines')
            (td/'caption.txt').write_text('\n'.join(lines),encoding='utf-8')
            (td/'number.txt').write_text(f'{i+1:02d} / {len(scenes):02d}',encoding='utf-8')
            filters="drawbox=x=76:y=108:w=136:h=16:color=0xE8FC6A:t=fill,drawtext=fontfile=font.ttf:text='CONTENT STUDIO / CLASSROOM':fontcolor=0xE8FC6A:fontsize=42:x=76:y=184,drawtext=fontfile=font.ttf:textfile=caption.txt:expansion=none:fontcolor=white:fontsize=68:line_spacing=28:x=76:y=(h-text_h)/2,drawtext=fontfile=font.ttf:textfile=number.txt:fontcolor=0xE8FC6A:fontsize=48:x=76:y=1570,drawtext=fontfile=font.ttf:text='SYNTHETIC CLASSROOM EXAMPLE':fontcolor=0xC3CBCF:fontsize=34:x=76:y=1712,drawtext=fontfile=font.ttf:text='SILENT CAPTIONS / NO VOICEOVER':fontcolor=0xC3CBCF:fontsize=32:x=76:y=1780"
            part=td/f'part{i}.mp4'
            cmd=[ffmpeg,'-hide_banner','-loglevel','error','-y','-f','lavfi','-i','color=c=0x102D35:s=1080x1920:r=30','-t',str(scene['duration_seconds']),'-vf',filters,'-an','-c:v','libx264','-preset','veryfast','-crf','24','-pix_fmt','yuv420p','-threads','2',str(part)]
            try: subprocess.run(cmd,cwd=td,check=True,capture_output=True,timeout=90)
            except (subprocess.SubprocessError,OSError) as e: raise WorkflowError('FFmpeg rendering failed; no finished video was produced. Verify the FFmpeg build supports drawtext and libx264') from e
            parts.append(part)
        (td/'concat.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
        subprocess.run([ffmpeg,'-hide_banner','-loglevel','error','-y','-f','concat','-safe','0','-i','concat.txt','-c','copy','-movflags','+faststart',str(output)],cwd=td,check=True,capture_output=True,timeout=30)
    probe=json.loads(subprocess.check_output([ffprobe,'-v','error','-show_streams','-show_format','-of','json',str(output)],timeout=15))
    v=next(s for s in probe['streams'] if s['codec_type']=='video')
    return {'duration':float(probe['format']['duration']),'width':v['width'],'height':v['height'],'codec':v['codec_name'],'frame_rate':v['r_frame_rate'],'audio_streams':sum(s['codec_type']=='audio' for s in probe['streams']),'voiceover':False,'renderer':'fixed local FFmpeg template','bytes':output.stat().st_size}

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');args=p.parse_args()
    data=json.loads(Path(args.input).read_text());data=data.get('artifacts',data)
    validate_artifacts(data);print(json.dumps(render(data['video'],args.output),indent=2))
