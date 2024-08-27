import yt_dlp
import os
import sys
import subprocess

def get_ffmpeg_path():
    try:
        result = subprocess.run(['pipenv', 'run', 'which', 'ffmpeg'], 
                                capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        print("Error: Unable to find ffmpeg path.")
        return None

def download_video(url):
    print(f"Python version: {sys.version}")
    print(f"yt-dlp version: {yt_dlp.version.__version__}")
    
    ffmpeg_path = get_ffmpeg_path()
    if not ffmpeg_path:
        print("Error: ffmpeg not found. Please ensure it's installed correctly.")
        return None

    print(f"Using ffmpeg from: {ffmpeg_path}")
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
        'verbose': True,
        'ffmpeg_location': ffmpeg_path,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Starting download...")
            info_dict = ydl.extract_info(url, download=True)
            print("Download completed.")
            video_title = info_dict.get('title', None)
            if video_title:
                return f"{video_title}.mp3"
            else:
                raise ValueError("Could not retrieve video title")
    except yt_dlp.utils.DownloadError as e:
        print(f"An error occurred while downloading the video: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return None