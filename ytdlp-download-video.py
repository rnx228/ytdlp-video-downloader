import tkinter as tk
from tkinter import messagebox
import os
import yt_dlp
import threading
import sys

def paste(event=None):
    try:
        clipboard = root.clipboard_get()
        url_entry.insert(tk.INSERT, clipboard)
    except tk.TclError:
        pass  # clipboard empty or non-text

def show_context_menu(event):
    context_menu.tk_popup(event.x_root, event.y_root)

def download_video():
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Warning", "Please enter a video URL")
        return

    def worker():
        try:
            downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
            ydl_opts = {
                'outtmpl': os.path.join(downloads_path, '%(title)s.%(ext)s'),
                'format': 'best',
                'quiet': True,
                'no_warnings': True,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            messagebox.showinfo("Success", f"Video downloaded to {downloads_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to download video:\n{e}")

    # Run download in a thread to keep GUI responsive
    threading.Thread(target=worker).start()

root = tk.Tk()
root.title("Facebook Video Downloader")

tk.Label(root, text="Video URL:").pack(padx=10, pady=(10,0))

url_entry = tk.Entry(root, width=60)
url_entry.pack(padx=10, pady=5)

# Right-click context menu
context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="Paste", command=paste)

url_entry.bind("<Button-3>", show_context_menu)  # Right-click for Windows/Linux
url_entry.bind("<Control-Button-1>", show_context_menu)  # macOS alternative

download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack(padx=10, pady=10)

root.mainloop()
