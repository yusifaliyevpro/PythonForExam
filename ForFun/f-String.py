adlar = ["Yusif", "Əli", "Günel", "Elmin"]
status = ["Məlumat tapılmadı", "Oxuyur", "Orta", "İstefa verib"]

for i in range(0, len(adlar)):
    print(f"{adlar[i]}: {status[i]}")

# Output:
# Yusif: Məlumat tapılmadı
# Əli: Oxuyur
# Günel: Orta
# Elmin: İstefa verib
