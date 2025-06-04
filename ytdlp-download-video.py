import os
import yt_dlp
import tkinter as tk
from tkinter import messagebox
from pathlib import Path

# --- FUNCTION ---
def download_video():
    video_url = url_entry.get().strip()
    if not video_url:
        messagebox.showwarning("Input Error", "Please enter a Facebook video URL.")
        return

    try:
        # Get user's Downloads folder path (Windows)
        downloads_path = Path.home() / "Downloads"
        downloads_path.mkdir(exist_ok=True)

        ydl_opts = {
            'outtmpl': str(downloads_path / '%(title)s.%(ext)s'),
            'quiet': False,
            'noplaylist': True,
            'format': 'bestvideo+bestaudio/best',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        messagebox.showinfo("Success", f"Download complete!\nSaved to:\n{downloads_path}")

    except Exception as e:
        messagebox.showerror("Error", f"Download failed: {e}")

# --- GUI SETUP ---
root = tk.Tk()
root.title("Facebook Video Downloader")
root.geometry("400x150")

tk.Label(root, text="Paste Facebook video URL:").pack(pady=(10, 5))

url_entry = tk.Entry(root, width=50)
url_entry.pack(padx=10)

tk.Button(root, text="Download Video", command=download_video).pack(pady=15)

root.mainloop()
