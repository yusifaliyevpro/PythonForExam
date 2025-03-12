# 3. (Orta Çətin): Banco Vaticano adlı bir bank müştərilərinə kredit limiti təyin etmək üçün xüsusi bir alqoritmdən istifadə edir.
# Bank müştəridən aldığı "Yaşınız?" və "Maaşınız?" suallarının cavabı əsasında, 18 yaşı tamam olmuş hər müştəriyə
# maaşının kvadratının 10%-i qədər pul verir. Lakin bu pul müştəriyə çatmazdan əvvəl 11% faiz komissiya çıxılır.
# Həmçinin bu Bank 65 yaş yuxarı müştərilərindən əlavə 23% sığorta məbləği alır.
# Sizsə əgər yaşınız uyğundursa, bu bankın sizə sonda verəcəyi məbləği, əks halda "Yaşınız 18-dən azdır" mesajını çap edən proqram yazın
# Nümunə1:
# Yaşınız?: 82
# Maaşınız?: 350
# Çıxış: 8394.925

# Nümunə2:
# Yaşınız?: 55
# Maaşınız?: 350
# Çıxış: 10902.5

# Nümunə3:
# Yaşınız?: 14
# Maaşınız?: 800
# Çıxış: "Yaşınız 18-dən azdır"

yaş = int(input("Yaşınız?: "))
maaş = int(input("Maaşınız?: "))
kredit = 0
if 18 <= yaş:
    kredit = kredit + maaş**2*10/100
    kredit = kredit - kredit*11/100
    if 65 < yaş:
        kredit = kredit - kredit*23/100
    print(kredit)
else:
    print("Yaşınız 18-dən azdır")
