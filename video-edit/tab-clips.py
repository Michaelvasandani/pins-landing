"""Cut the four raw screen recordings into short looping clips for the capability tabs on prototype C.

Each clip keeps only the moments that show Pins working; waits are sped up.
Run from anywhere: python3 video-edit/tab-clips.py
"""
from pathlib import Path
import subprocess

R = Path(__file__).resolve().parent
SRC = R.parent / 'raw_video'
OUT = R.parent / 'prototypes' / 'c-video-downloader' / 'media'
OUT.mkdir(parents=True, exist_ok=True)

WIDTH = 1440  # rendered at ~2x the tab panel's on-page width
FPS = 30

# name: (source, crop x/y/w/h in source pixels, [(start, end, speed), ...])
CLIPS = {
    # Video found, Pin video, recording (sped up), saved, My Pins, open it from the library.
    # Starts after the extension menu so the account name and email never show.
    'pin-video': ('video_2.mov', (380, 270, 2644, 1640), [
        (3.8, 5.0, 1), (5.0, 11.0, 4), (11.0, 13.0, 1), (13.0, 15.6, 1.25), (17.2, 20.3, 1.25), (20.3, 22.8, 1)]),
    # Detect images on this page, select the grid (sped up), pin, images appear in My Pins
    'pin-images': ('image.MOV', (380, 270, 2644, 1640), [
        (5.5, 7.0, 1), (7.0, 15.0, 2.5), (15.0, 18.3, 1.5), (22.2, 24.5, 1)]),
    # Pin a post on X: Post found, pin it, the post lands in My Pins
    'pin-post': ('tweet.MOV', (380, 270, 2644, 1640), [
        (2.0, 9.0, 1.25), (10.4, 12.2, 1)]),
    # Scroll the My Pins library, open a video, Download
    'my-pins': ('Gallery.MOV', (220, 270, 2730, 1694), [
        (0.0, 7.5, 1.25), (7.8, 9.5, 1), (11.0, 13.5, 1)]),
}


def build(name, src, crop, segments):
    x, y, w, h = crop
    parts = []
    for i, (a, b, speed) in enumerate(segments):
        parts.append(
            f'[0:v]trim=start={a}:end={b},setpts=(PTS-STARTPTS)/{speed},'
            f'fps={FPS},crop={w}:{h}:{x}:{y},scale={WIDTH}:-2:flags=lanczos,setsar=1[s{i}]')
    parts.append(''.join(f'[s{i}]' for i in range(len(segments))) + f'concat=n={len(segments)}:v=1:a=0[out]')
    mp4 = OUT / f'{name}.mp4'
    subprocess.run([
        'ffmpeg', '-y', '-hide_banner', '-loglevel', 'error', '-i', str(SRC / src),
        '-filter_complex', ';'.join(parts), '-map', '[out]', '-an',
        '-c:v', 'libx264', '-preset', 'slow', '-crf', '24', '-pix_fmt', 'yuv420p', '-movflags', '+faststart',
        str(mp4)], check=True)
    # Poster: first frame, shown before the clip loads and for reduced motion
    subprocess.run([
        'ffmpeg', '-y', '-hide_banner', '-loglevel', 'error', '-i', str(mp4),
        '-frames:v', '1', '-q:v', '3', str(OUT / f'{name}.jpg')], check=True)
    print(name, 'done', flush=True)


for name, (src, crop, segments) in CLIPS.items():
    build(name, src, crop, segments)
