# 3. Verilmiş n ədədinin pifaqor ədədi olub olmadığını yoxlayan proqram yazın.

a = []
for i in range(1, 4):
    a.append(int(input(f"{i} saylı ədədi daxil edin: ")))
a.sort()
a, b, c = a

if a**2+b**2 == c**2:
    print("Pifaqor ədədləridir")
else:
    print("Pifaqor ədədləri deyil")
