import requests
import base64
import os

# API URL ve başlıklar
url = "https://api-lms.aztu.edu.az/api/exam-results/43d456c2-36f9-6e46-a653-da6b5dba044b/questions"

headers = {
    "Accept": "application/json, text/plain, */*",
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vYXBpLWxtcy5henR1LmVkdS5hei9hcGkvbG9naW4iLCJpYXQiOjE3NDk2Njk1NDgsImV4cCI6MTc0OTY3Njc0OCwibmJmIjoxNzQ5NjY5NTQ4LCJqdGkiOiJnck5YY3cxbWk3YXN4MEdxIiwic3ViIjoiMjAyNDA2MzYwIiwicHJ2IjoiZjdjNWVkNjRlODZkNDE5NTVhYjNmN2MxZDMzOGE4NTcwZjVhZWVjZSIsInVzZXJfdHlwZSI6IlMiLCJlIjoiZXlKcGRpSTZJa1ZhWTJkV1EwVnRXV0ZCV1c0MWFVZGtZblkwTWxFOVBTSXNJblpoYkhWbElqb2lSbmRqVEM5T1pIQkZWRmhZVEVobk0wc3hjV2xuZG01YVdGbEhVMk50UVhjclNra3ZibVJtZEZKWk0xaEJXVTFYVTNWclRERkxaM05IZVZJM1NUUlZWRmgxTlN0R2VrdzJkV05uY1ZCTFJVWlBZMmx1WjJoWlNsWXpaMlJHV0ZWak9VdElVV3RLWW5ZcmJuUjJPWEJWV1hSVU1FWmplbkowUkZoNGRIVTBSVU0wZFZGSlZqQnNlRzFMV0hwTEszUndZMlpsT0ZSdlZHeFJUbWxsY2tSdFZHRlJXazFaZUZsR0syMVdaekpRTDJ0Q2JDdFpPV1I2TkdOc1prUlBZVmMxSWl3aWJXRmpJam9pTmpJNE56QXpaR1ZoWXpGaU9XUmpNMll3WW1Vd09EZGlPR0kxTlRrd05qZzROV1k0WlRKa1pEUXpOMlE0TXpRNFpHRm1OVFF6TnpBeU4yVm1NV0l6TXlJc0luUmhaeUk2SWlKOSJ9.YzAuSY6wgrZYk_G9qI-s1GaUSfMcC-60V4nqmcpJv_Y",
    "Origin": "https://lms.aztu.edu.az",
    "Referer": "https://lms.aztu.edu.az/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 OPR/119.0.0.0",
}

# Klasör yolu
folder_path = "questions-os"

# Klasör yoksa oluştur
os.makedirs(folder_path, exist_ok=True)

# İstek gönder
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("İstek başarılı!")
    data = response.json()

    image_count = 1
    for q_index, question in enumerate(data.get("questions", []), start=1):
        if question["attachment"]:
            try:
                image_data = base64.b64decode(question["attachment"])
                filename = os.path.join(folder_path, f"q{image_count}.png")
                with open(filename, "wb") as f:
                    f.write(image_data)
                print(f"{filename} kaydedildi.")
            except Exception as e:
                print(f"Hata oluştu (soru {q_index}, cevap {1}): {e}")
        for ans_index, student_answer in enumerate(
            question.get("studentAnswers", []), start=1
        ):
            if student_answer.get("isImageContent") and student_answer.get(
                "attachment"
            ):
                base64_str = student_answer["attachment"]
                try:
                    image_data = base64.b64decode(base64_str)
                    filename = os.path.join(folder_path, f"{image_count}.png")
                    with open(filename, "wb") as f:
                        f.write(image_data)
                    print(f"{filename} kaydedildi.")
                    image_count += 1
                except Exception as e:
                    print(f"Hata oluştu (soru {q_index}, cevap {ans_index}): {e}")
else:
    print(f"Hata oluştu: {response.status_code}")
    print(response.text)
