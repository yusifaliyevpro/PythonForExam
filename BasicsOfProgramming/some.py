import requests
from bs4 import BeautifulSoup
import json

# Tüm verileri kaydedeceğimiz liste
all_data = []
id_ = 1

# 1'den 50'ye kadar olan sayfaları dolaşan döngü
for page_num in range(1, 51):  # Sayfa numaraları 1'den 50'ye kadar
    # Dinamik URL
    url = f"https://www.testbook.az/word/{page_num}"

    # Web sayfasına istek gönder ve içeriği al
    response = requests.get(url)
    html_content = response.content

    # HTML içeriğini BeautifulSoup ile parse et
    soup = BeautifulSoup(html_content, "html.parser")

    # table > tbody > tr yapısındaki tr taglarını bul
    rows = soup.find_all("tr")

    # Her sayfa için verileri toplama
    for row in rows[1:]:  # İlk başlık satırını [1:] ile geçiyoruz
        # tr içindeki tüm td taglarını bul
        tds = row.find_all("td")

        if len(tds) >= 3:  # En az 3 td olması gerekiyor
            # İlk td ID, ikinci td İngilizce, üçüncü td Azerbaycan tercümesi
            english = tds[1].text.strip()
            azerbaijani = tds[2].text.strip()

            # Verileri bir sözlük yapısına ekle
            data_dict = {"id": id_, "en": english, "az": azerbaijani}

            # Tüm verilere ekle
            all_data.append(data_dict)
            id_ += 1

# Tüm verileri JSON formatında dosyaya yaz
with open("data.json", "w", encoding="utf-8") as json_file:
    json.dump(all_data, json_file, ensure_ascii=False, indent=4)

print(f"Toplam {len(all_data)} veri data.json dosyasına kaydedildi.")
