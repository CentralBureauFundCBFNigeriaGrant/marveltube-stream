import subprocess, time

STREAM_KEY = "YOUR_STREAM_KEY"
VIDEO_LIST = [
    "https://github.com/CentralBureauFundCBFNigeriaGrant/marveltube-stream/releases/download/V2.0/I.Tried.Cooking.For.My.Wife.in.10.Minutes.I.FAILED.720p._1778229740240.mp4",
    "https://github.com/CentralBureauFundCBFNigeriaGrant/marveltube-stream/releases/download/V2.0/Does.Your.Background.Really.Matter.To.Go.Viral.on.YouTube._.A.MUST.WATCH.FOR.NEW.CREATORS.1080p._1778228673635.mp4",
]

with open("playlist.txt", "w") as f:
    for url in VIDEO_LIST:
        f.write(f"file '{url}'\n")

while True:
    cmd = [
        "ffmpeg", "-re", "-stream_loop", "-1", "-f", "concat",
        "-i", "playlist.txt",
        "-vf", "scale=1280:-2",
        "-c:v", "libx264", "-preset", "superfast",
        "-b:v", "2000k", "-maxrate", "2000k", "-bufsize", "4000k",
        "-g", "60", "-keyint_min", "60",
        "-r", "30", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "128k", "-ar", "44100",
        "-f", "flv", f"rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}"
    ]
    process = subprocess.run(cmd)
    print("Stream crashed. Restarting in 5s...")
    time.sleep(5)
