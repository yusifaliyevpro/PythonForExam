import json

# Dosya yolları
input_file = "packages.json"
output_file = "transformed_packages.json"


# JSON dönüştürme fonksiyonu
def transform_package(data):
    transformed = []
    for item in data:
        package = item.get("package", {})
        all_questions = []
        for phase in package.get("phases", []):
            questions = phase.get("questions", [])
            if questions is None:  # Eğer "questions" None ise atla
                continue
            for question in questions:
                # İlgili alanları seç
                question_data = {
                    "comment": question.get("comment"),
                    "considered": question.get("considered"),
                }
                # Values içindeki ilk öğeden text, answer ve rekvizit alınır
                first_value = question.get("values", [{}])[0]
                question_data.update(
                    {
                        "question": first_value.get("text"),
                        "answer": first_value.get("answer"),
                        "rekvizit": first_value.get("rekvizit"),
                    }
                )
                all_questions.append(question_data)

        transformed_item = {
            "id": package.get("id"),
            "name": package.get("name"),
            "information": package.get("information"),
            "gameType": package.get("game", {}).get("id"),  # game içindeki id'yi al
            "editors": [
                editor.get("fullname") for editor in package.get("editors", [])
            ],
            "questions": all_questions,
        }
        transformed.append(transformed_item)
    return transformed


# JSON verisini okuyup dönüştürme
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)  # packages.json'daki veriyi yükle

# Dönüştür
transformed_data = transform_package(data)

# Dönüştürülmüş veriyi kaydet
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(transformed_data, f, ensure_ascii=False, indent=4)

print(f"Dönüştürme tamamlandı! Sonuç dosyası: {output_file}")
