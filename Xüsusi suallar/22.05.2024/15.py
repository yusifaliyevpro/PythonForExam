# 15. Verilmiş a siyahısında olan ədədlərin ədədi ortasından böyük olan ədədlərdən yeni bir b siyahısı yaradan proqramı yazın.

a = []
b = []
n = int(input("Neçə ədəd daxil edəcəksiz?: "))

for i in range(1, n+1):
    a.append(float(input(f"{i} saylı ədədi daxil edin: ")))

ave = sum(a)/len(a)

for i in a:
    if i > ave:
        b.append(i)
print(b)
