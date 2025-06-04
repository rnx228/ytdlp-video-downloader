import os
import yt_dlp

def download_facebook_video(url):
    downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads/Video')
    ydl_opts = {
        'outtmpl': os.path.join(downloads_path, '%(title)s.%(ext)s'),
        'format': 'best',
        'quiet': False,
        'no_warnings': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"\n✅ Download completed. Saved to: {downloads_path}")
    except Exception as e:
        print(f"\n❌ Failed to download video:\n{e}")

if __name__ == '__main__':
    url = input("Enter Facebook video URL: ").strip()
    if url:
        download_facebook_video(url)
    else:
        print("⚠️ No URL provided. Exiting.")
