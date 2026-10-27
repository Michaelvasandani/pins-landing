from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import subprocess
R=Path(__file__).resolve().parent; W=R/'work'; O=R/'exports'
SRC=R.parent/'Screen Recording 2026-10-27 at 11.14.45.MOV'
font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',30)
captions=[('Pin a video',0.5,4.1),('Save it to My Pins',8.2,12.0),('Download your clip',16.1,19.3),('Downloaded',20.0,21.7)]
for i,(text,a,b) in enumerate(captions):
 im=Image.new('RGBA',(1920,1080),(0,0,0,0));d=ImageDraw.Draw(im)
 tw=d.textlength(text,font=font);left=int((1920-tw-64)/2)
 d.rounded_rectangle((left,966,1920-left,1030),radius=32,fill=(20,23,21,225))
 d.text(((1920-tw)/2,982),text,font=font,fill='white')
 im.save(W/f'v2-caption-{i}.png')
# Continuous source order. Only the waiting portions are sped up.
clips=[(1.8,7.8,1),(7.8,12.6,4),(12.6,20.8,1),(20.8,23.3,2.5),(23.3,28.6,1)]
f=["[0:v]drawbox=x=2318:y=702:w=660:h=108:color=0x454746:t=fill:enable='between(t,2.1,4.5)',split=5"+''.join(f'[s{i}]' for i in range(5))]
for i,(a,b,s) in enumerate(clips): f.append(f'[s{i}]trim=start={a}:end={b},setpts=(PTS-STARTPTS)/{s},fps=30[c{i}]')
f.append(''.join(f'[c{i}]' for i in range(5))+'concat=n=5:v=1:a=0,crop=3024:1700:0:140[cut]')
# Eased camera moves remain continuous across time-compressed capture and library waits.
keys=[(0,1,1),(1.5,1.35,1),(11.4,1.35,1),(12.7,1.1,0),(14.5,1.1,0),(15.8,1,0),(17.6,1.65,1),(19.0,1.65,1),(20.1,2,1),(21.7,2,1)]
def expr(column):
 e=str(keys[-1][column])
 for k in range(len(keys)-2,-1,-1):
  a,b=keys[k],keys[k+1];p=f'clip((on/30-{a[0]})/{b[0]-a[0]},0,1)';smooth=f'({p}*{p}*(3-2*{p}))'
  v=f'({a[column]}+({b[column]-a[column]})*{smooth})'
  e=f'if(lt(on/30,{b[0]}),{v},{e})'
 return e
z=expr(1);x=f'(iw-iw/zoom)*({expr(2)})'
f.append(f"[cut]zoompan=z='{z}':x='{x}':y=0:d=1:s=1920x1080:fps=30,setsar=1[cam]")
prev='cam'
for i,(_,a,b) in enumerate(captions):
 f.append(f'[{i+1}:v]format=rgba,fade=t=in:st={a}:d=0.22:alpha=1,fade=t=out:st={b-0.22}:d=0.22:alpha=1[cap{i}]')
 f.append(f'[{prev}][cap{i}]overlay=0:0:shortest=1[v{i}]');prev=f'v{i}'
(W/'v2-filter.txt').write_text(';\n'.join(f))
cmd=['ffmpeg','-y','-hide_banner','-loglevel','error','-i',str(SRC)]
for i in range(len(captions)):cmd+=['-loop','1','-framerate','30','-i',str(W/f'v2-caption-{i}.png')]
cmd+=['-filter_complex_script',str(W/'v2-filter.txt'),'-map',f'[{prev}]','-t','21.7','-an','-c:v','libx264','-preset','fast','-crf','19','-pix_fmt','yuv420p','-movflags','+faststart',str(O/'frevana-pins-download-demo-v2.mp4')]
subprocess.run(cmd,check=True)
print('v2 exported',flush=True)
