# 10. Verilmiş n natural ədədinin tək rəqəmlərinin ədədi ortasını hesablayan proqram yazın.

n = input("Ədəd daxil edin: ")
s = 0

for i in n:
    i = int(i)
    if i % 2 == 1:
        s += i
print(s / len(n))
