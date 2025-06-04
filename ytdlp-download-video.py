import yt_dlp
import os

# --- CONFIGURATION ---
url = ""  # Paste your Facebook video URL here
output_path = os.path.join(os.path.dirname(__file__), 'downloads')  # Save in "downloads" folder

# Create output directory if it doesn't exist
os.makedirs(output_path, exist_ok=True)

# --- FUNCTION ---
def download_facebook_video(video_url, save_path):
    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        'quiet': False,
        'noplaylist': True,
        'format': 'bestvideo+bestaudio/best',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

# --- RUN ---
download_facebook_video(url, output_path)
