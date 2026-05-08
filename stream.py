import subprocess, time

STREAM_KEY = "1dr5-f1jq-bspa-qbee-2yda"  # <-- PUT YOUR REAL STREAM KEY HERE
VIDEO_LIST = [
    "https://youtu.be/RlFBKJFCzO4?si=xYgGDNpoopNP46oZ",
    "https://youtu.be/8n3BBc-_ygA?si=tZ2fqAY1g_CrYF8C"
]

# Write playlist
with open("playlist.txt", "w") as f:
    for url in VIDEO_LIST:
        f.write(f"file '{url}'\n")

# Start infinite loop stream
while True:
    cmd = [
        "ffmpeg", "-re", "-stream_loop", "-1", "-f", "concat",
        "-i", "playlist.txt", "-c", "copy",
        "-f", "flv", f"rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}"
    ]
    process = subprocess.run(cmd)
    print("Stream crashed. Restarting in 5s...")
    time.sleep(5)
