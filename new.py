import os
import shutil
from pathlib import Path

# Kullanıcının Downloads klasörünü al
DOWNLOADS_FOLDER = Path("C:/Users/yusif/Downloads")  # Burada yolu direkt yazıyoruz

# Dosya türlerine göre klasörler
FILE_CATEGORIES = {
    "Images": [
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
        ".svg",
        ".tiff",
        ".webp",
        ".heif",
    ],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv", ".webm"],
    "Documents": [
        ".pdf",
        ".docx",
        ".doc",
        ".xls",
        ".txt",
        ".xlsx",
        ".pptx",
        ".ppt",
        ".odt",
        ".rtf",
        ".md",
        ".tex",
        ".epub",
        ".mobi",
        ".azw3",
    ],
    "Software": [".exe", ".msi", ".dmg"],
    "Compressed": [".zip", ".rar", ".7z", ".tar.gz", ".tar.bz2", ".xz", ".tar"],
    "Music": [".mp3", ".wav", ".flac"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
    "Code": [
        ".html",
        ".js",
        ".jsx",
        ".ts",
        ".tsx",
        ".css",
        ".php",
        ".py",
        ".java",
        ".rb",
        ".go",
        ".cpp",
        ".h",
        ".sh",
        ".ipynb",
        ".sql",
        ".json",
    ],
    "Digital Art": [".ai", ".psd", ".xd", ".fig"],
    "Others": [],
}


def organize_downloads():
    if not DOWNLOADS_FOLDER.exists():
        print("Downloads klasörü bulunamadı!")
        return

    # Downloads klasöründeki her dosyayı kontrol et
    for item in DOWNLOADS_FOLDER.iterdir():
        if item.is_file():
            moved = False
            for category, extensions in FILE_CATEGORIES.items():
                if item.suffix.lower() in extensions:
                    category_folder = DOWNLOADS_FOLDER / category
                    category_folder.mkdir(exist_ok=True)
                    try:
                        shutil.move(str(item), str(category_folder / item.name))
                    except Exception as e:
                        print(f"Hata: {item.name} taşınamadı: {e}")
                    moved = True
                    break

            # Eğer kategoriye uymuyorsa "Others" klasörüne at
            if not moved:
                others_folder = DOWNLOADS_FOLDER / "Others"
                others_folder.mkdir(exist_ok=True)
                try:
                    shutil.move(str(item), str(others_folder / item.name))
                except Exception as e:
                    print(f"Hata: {item.name} taşınamadı: {e}")

    # Şimdi, kategori klasörlerinde yanlış yerleşmiş dosyaları kontrol et
    for category, extensions in FILE_CATEGORIES.items():
        category_folder = DOWNLOADS_FOLDER / category
        if category_folder.exists():
            for item in category_folder.iterdir():
                if item.is_file():
                    for correct_category, correct_extensions in FILE_CATEGORIES.items():
                        if (
                            item.suffix.lower() in correct_extensions
                            and correct_category != category
                        ):
                            correct_folder = DOWNLOADS_FOLDER / correct_category
                            correct_folder.mkdir(exist_ok=True)
                            try:
                                shutil.move(str(item), str(correct_folder / item.name))
                                print(
                                    f"{item.name} {category} klasöründen {correct_category} klasörüne taşındı."
                                )
                            except Exception as e:
                                print(f"Hata: {item.name} taşınamadı: {e}")
                            break


if __name__ == "__main__":
    organize_downloads()
    print("Download klasörü düzenlendi!")
