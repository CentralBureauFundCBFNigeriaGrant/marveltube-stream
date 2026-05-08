import subprocess, time, os, requests

STREAM_KEY = "YOUR_STREAM_KEY"   # ← Paste your real stream key here

VIDEO_LIST = [
    "https://github.com/CentralBureauFundCBFNigeriaGrant/marveltube-stream/releases/download/V2.0/I.Tried.Cooking.For.My.Wife.in.10.Minutes.I.FAILED.720p._1778229740240.mp4",
    "https://github.com/CentralBureauFundCBFNigeriaGrant/marveltube-stream/releases/download/V2.0/Does.Your.Background.Really.Matter.To.Go.Viral.on.YouTube._.A.MUST.WATCH.FOR.NEW.CREATORS.1080p._1778228673635.mp4"
]

LOCAL_FILES = []

# Download videos once with simple names
for i, url in enumerate(VIDEO_LIST):
    local_name = f"v{i}.mp4"
    if not os.path.exists(local_name):
        print(f"Downloading {url} → {local_name}")
        r = requests.get(url, stream=True)
        r.raise_for_status()
        with open(local_name, 'wb') as f:
            for chunk in r.iter_content(8192):
                f.write(chunk)
    else:
        print(f"Already cached: {local_name}")
    LOCAL_FILES.append(local_name)

# Write playlist of local files
with open("playlist.txt", "w") as f:
    for name in LOCAL_FILES:
        f.write(f"file '{name}'\n")

# Begin 24/7 loop with optimized settings
while True:
    cmd = [
        "ffmpeg", "-re", "-stream_loop", "-1",
        "-f", "concat", "-safe", "0", "-i", "playlist.txt",
        "-vf", "scale=1280:-2",
        "-c:v", "libx264", "-preset", "superfast",
        "-b:v", "2000k", "-maxrate", "2000k", "-bufsize", "4000k",
        "-g", "60", "-keyint_min", "60",
        "-r", "30", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "128k", "-ar", "44100",
        "-f", "flv", f"rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}"
    ]
    process = subprocess.run(cmd)
    print("Stream dropped. Restarting in 5s...")
    time.sleep(5)
