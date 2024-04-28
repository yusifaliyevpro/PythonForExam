# Sətirdə yer alan rəqəmlərin kvadratları cəmini çap edən proqram

a = input("Hərf və rəqəmlərdən ibarət cümlə daxil edin: ")
b = 0  # Toplama əməli edəcəyimiz üçün b-ə sıfır veririk

for i in a:
    if i.isdigit():  # Rəqəmdirsə True, adi simvoldursa False verir
        b = b + int(i)**2
print(b)

# Input: yusifaliyevpro2024
# Output: 24
