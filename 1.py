a = input("Hərf və rəqəmlərdən ibarət cümlə daxil edin: ")
b = 0  # Toplama əməli edəcəyimiz üçün b-ə sıfır veririk

for i in a:
    if i.isdigit():  # Rəqəmdirsə True, adi simvoldursa False verir
        b = b + int(i)**2
print(b)
