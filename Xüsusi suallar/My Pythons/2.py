# 2. (Orta səviyyəli) Klaviaturadan daxil edilmiş sətirdə 7-dən kiçik ədədlərin kvadratları cəmini hesablayan, heç bir rəqəm olmaması və ya cəmin sıfıra bərabər olması halında isə ekrana "Bəxtinizi bir daha sınayın" çıxardan proqramı yazın
# Nümunə
# Giriş: Helloo_632-1492
# Output: 70

a = input("Sətiri daxil edin: ")
s = 0

for i in a:
    if i.isdigit() and int(i) < 7:
        i = int(i)
        s += i**2

if s == 0:
    print("Bəxtinizi bir daha sınayın")
else:
    print(s)
