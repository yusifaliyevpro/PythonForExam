import requests
import json

# JSON dosyasına kaydedilecek verilerin tutulduğu liste
all_packages = []

# URL'yi oluşturmak için temel URL
base_url = "https://api.3sual.az/api/packages/foruse?id="

# Kontrol etmek istediğimiz aralık
start_id = 141
end_id = 1741

# Belirli aralıkta `id`leri döngüyle kontrol ediyoruz
for package_id in range(start_id, end_id + 1):
    if not package_id in range(641, 1641):
        try:
            # İstek URL'si
            url = f"{base_url}{package_id}"

            # API'ye GET isteği gönderiliyor
            response = requests.get(url)

            # JSON verisini ayrıştırma
            if response.status_code == 200:
                data = response.json()

                # Status kontrolü ve `game.id` kontrolü
                if "package" in data and data["package"]["game"]["id"] == 2:
                    # Soruları kontrol et
                    phases = data["package"].get("phases", [])
                    has_questions = any(
                        phase.get("themes")
                        for phase in phases
                        if len(phase.get("themes", [])) > 0
                    )

                    # Eğer en az bir question varsa, paketi kaydet
                    if has_questions:
                        all_packages.append(data)
                        print(f"{package_id} ✅")
                    else:
                        print(f"{package_id} ❌❌")
                else:
                    print(f"{package_id} ❌")

        except Exception as e:
            print(f"ID {package_id} işleminde hata: {e}")

# Tüm verileri JSON dosyasına kaydetme
output_file = "packages.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(all_packages, f, ensure_ascii=False, indent=4)

print(f"{len(all_packages)} adet paket JSON dosyasına kaydedildi.")
