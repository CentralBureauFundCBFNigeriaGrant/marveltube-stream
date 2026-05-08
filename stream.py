import subprocess, time

STREAM_KEY = "1dr5-f1jq-bspa-qbee-2yda"
VIDEO_LIST = [
    "https://github.com/CentralBureauFundCBFNigeriaGrant/marveltube-stream/releases/latest/download/I.Tried.Cooking.For.My.Wife.in.10.Minutes.I.FAILED.720p._1778229740240.mp4",
    "https://github.com/CentralBureauFundCBFNigeriaGrant/marveltube-stream/releases/latest/download/Does.Your.Background.Really.Matter.To.Go.Viral.on.YouTube._.A.MUST.WATCH.FOR.NEW.CREATORS.1080p._1778228673635.mp4"
]

# Write playlist
with open("playlist.txt", "w") as f:
    for url in VIDEO_LIST:
        f.write(f"file '{url}'\n")

# Start infinite loop stream
while True:
    cmd = [
        "ffmpeg", "-re", "-f", "concat", "-safe", "0",
        "-stream_loop", "-1", "-i", "playlist.txt",
        "-c", "copy",
        "-f", "flv", f"rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}"
    ]
    process = subprocess.run(cmd)
    print("Stream crashed. Restarting in 5s...")
    time.sleep(5)
