import subprocess, time, os

STREAM_KEY = "1dr5-f1jq-bspa-qbee-2yda"

VIDEO_LIST = [
    "https://github.com/CentralBureauFundCBFNigeriaGrant/marveltube-stream/releases/download/V2.0/I.Tried.Cooking.For.My.Wife.in.10.Minutes.I.FAILED.720p._1778229740240.mp4",
    "https://github.com/CentralBureauFundCBFNigeriaGrant/marveltube-stream/releases/download/V2.0/Does.Your.Background.Really.Matter.To.Go.Viral.on.YouTube._.A.MUST.WATCH.FOR.NEW.CREATORS.1080p._1778228673635.mp4"
]

# Write the playlist file (still needed by the concat demuxer)
with open("playlist.txt", "w") as f:
    for url in VIDEO_LIST:
        f.write(f"file '{url}'\n")

# Build the FFmpeg command that will loop the playlist forever
# and push it to YouTube without ever dropping the connection
cmd = [
    "ffmpeg", "-re",
    "-f", "concat",
    "-safe", "0",
    "-protocol_whitelist", "file,https,tcp,tls",
    "-reconnect", "1",
    "-reconnect_at_eof", "1",
    "-reconnect_streamed", "1",
    "-reconnect_delay_max", "5",
    "-stream_loop", "-1",      # <-- infinite loop on the input
    "-i", "playlist.txt",
    "-c", "copy",
    "-f", "flv",
    f"rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}"
]

while True:
    print("Starting 24/7 stream...")
    process = subprocess.run(cmd)
    print(f"Stream ended with code {process.returncode}. Restarting in 5 seconds...")
    time.sleep(5)
