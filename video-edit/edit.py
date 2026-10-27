from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import subprocess, json
ROOT=Path(__file__).resolve().parent
SRC=ROOT.parent/'Screen Recording 2026-10-27 at 11.14.45.MOV'
WORK=ROOT/'work'; OUT=ROOT/'exports'
FONT='/System/Library/Fonts/Helvetica.ttc'
def font(n): return ImageFont.truetype(FONT,n)
steps=[
 ('Open Frevana', 'On the video page,\nopen Frevana and\nchoose Pin.'),
 ('Pin the video', 'Check the detected video.\nClick Pin video to\nstart capturing.'),
 ('Finish the capture', 'Click Stop recording\nwhen you have the\nclip you need.'),
 ('Find it in My Pins', 'Open My Pins, then\nselect your saved video.'),
 ('Download your clip', 'Click Download in\nthe saved video preview.'),
 ('Ready to use', 'Your video is downloaded\nas an MP4 file.')]
# Source in/out times, playback speed, step, crop x/y/w/h, hold at end.
shots=[
 (1.8,4.5,0.9,0,(1100,180,1920,1200),0),
 (4.5,7.7,0.9,1,(1100,180,1920,1200),0),
 (12.6,15.65,1,2,(1100,180,1920,1200),0),
 (15.65,17.6,1,3,(1100,180,1920,1200),0),
 (18.1,21.7,1,3,(0,240,3024,1720),0),
 (23.3,26.65,0.85,4,(1000,140,1800,1126),0),
 (26.65,28.8,1,5,(1810,150,1100,688),1.4),
]
INK='#1a1a1a'; GREEN='#4a6550'; MUTED='#686b66'
for i,(title,body) in enumerate(steps):
 im=Image.new('RGB',(1920,1080),'#fafafa');d=ImageDraw.Draw(im)
 # Minimal pin mark and wordmark.
 d.rounded_rectangle((64,48,104,88),radius=12,fill='#e7f0e8')
 d.ellipse((77,57,91,71),outline=GREEN,width=3);d.line((84,70,84,80),fill=GREEN,width=3)
 d.text((120,51),'Frevana Pins',font=font(30),fill=INK)
 d.text((64,111),'From video to download.',font=font(57),fill=INK)
 d.text((1635,64),'PRODUCT DEMO',font=font(18),fill=MUTED)
 d.line((64,197,1856,197),fill='#e4e7e2',width=2)
 d.rounded_rectangle((64,275,182,321),radius=23,fill='#e7f0e8')
 d.text((86,287),f'0{i+1} / 06',font=font(21),fill=GREEN)
 # Hand-wrapped titles for a clear narrow column.
 headings=['Open\nFrevana','Pin the\nvideo','Finish the\ncapture','Find it in\nMy Pins','Download\nyour clip','Ready\nto use']
 d.multiline_text((64,355),headings[i],font=font(52),fill=INK,spacing=9)
 d.multiline_text((66,516),body,font=font(27),fill=MUTED,spacing=14)
 if i==2: d.text((66,674),'Capture wait shortened',font=font(20),fill=GREEN)
 if i==5:
  d.rounded_rectangle((64,672,298,725),radius=26,fill='#e7f0e8')
  d.text((89,687),'Download complete',font=font(22),fill=GREEN)
 d.rounded_rectangle((550,218,1866,1000),radius=24,fill='#e6e9e3')
 d.rounded_rectangle((558,226,1858,992),radius=18,fill='#f3f3f1')
 for n in range(6):
  x=64+n*68
  d.rounded_rectangle((x,921,x+54,926),radius=2,fill=GREEN if n<=i else '#dfe3dd')
 d.text((64,1018),'PIN  /  SAVE  /  DOWNLOAD',font=font(18),fill=MUTED)
 d.text((1565,1018),'frevana.com',font=font(22),fill=MUTED)
 im.save(WORK/f'layout-{i}.png')
# Transparent rounded frame around the actual recording.
mask=Image.new('RGBA',(1296,760),(0,0,0,0));md=ImageDraw.Draw(mask)
md.rounded_rectangle((0,0,1295,759),radius=16,outline='#e6e9e3',width=2)
mask.save(WORK/'frame.png')
for k,(a,b,speed,step,crop,hold) in enumerate(shots):
 x,y,w,h=crop
 # Hide the account address on the opening extension menu only.
 privacy="drawbox=x=2318:y=728:w=660:h=82:color=0x454746:t=fill," if step==0 else ''
 filters=(f'[0:v]setpts=(PTS-STARTPTS)/{speed},{privacy}'
          f'crop={w}:{h}:{x}:{y},scale=1296:760:force_original_aspect_ratio=decrease,'
          f'pad=1296:760:(ow-iw)/2:(oh-ih)/2:color=0xf3f3f1,setsar=1,fps=30,'
          f'tpad=stop_mode=clone:stop_duration={hold}[clip];'
          '[1:v][clip]overlay=560:230:shortest=1[v]')
 duration=(b-a)/speed+hold
 cmd=['ffmpeg','-y','-hide_banner','-loglevel','error','-ss',str(a),'-t',str(b-a),'-i',str(SRC),
      '-loop','1','-i',str(WORK/f'layout-{step}.png'),'-filter_complex',filters,'-map','[v]',
      '-t',str(duration),'-an','-c:v','libx264','-preset','fast','-crf','19','-pix_fmt','yuv420p','-r','30',str(WORK/f'part-{k}.mp4')]
 subprocess.run(cmd,check=True)
 print(f'Rendered shot {k+1}/{len(shots)}',flush=True)
(WORK/'concat.txt').write_text(''.join(f"file '{WORK/f'part-{k}.mp4'}'\n" for k in range(len(shots))))
subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-f','concat','-safe','0','-i',str(WORK/'concat.txt'),'-c','copy','-movflags','+faststart',str(OUT/'frevana-pins-download-demo.mp4')],check=True)
subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-ss','4.2','-i',str(OUT/'frevana-pins-download-demo.mp4'),'-frames:v','1',str(OUT/'frevana-pins-poster.jpg')],check=True)
(ROOT/'edit-decisions.json').write_text(json.dumps({'source':SRC.name,'shots':shots,'output':'1920x1080, 30fps, H.264, silent, fast-start MP4','steps':steps},indent=2))
print('Export complete',flush=True)
