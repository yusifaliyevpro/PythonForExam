import yt_dlp
import os


def download_playlist_as_mp3(playlist_url):
    # İndirilen dosyaların kaydedileceği klasör
    save_path = "musics"
    # Klasör yoksa oluştur
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # yt-dlp ayarları
    ydl_opts = {
        "format": "bestaudio/best",  # En iyi ses kalitesini seç
        "outtmpl": os.path.join(save_path, "%(title)s.%(ext)s"),  # Kaydetme şablonu
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",  # MP3 formatına dönüştür
                "preferredquality": "192",  # Ses kalitesi: 192 kbps
            }
        ],
        "ignoreerrors": True,  # Hataları göz ardı et ve devam et
    }

    # İndirme işlemi
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])


# Kullanım:
playlist_url = (
    "https://www.youtube.com/playlist?list=PLR6KqQyoNvHOhNzuVxr7jmkJ6BXAYR7UD"
)
download_playlist_as_mp3(playlist_url)
