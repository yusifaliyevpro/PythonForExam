# 10. Verilmiş n natural ədədinin tək rəqəmlərinin ədədi ortasını hesablayan proqram yazın.

n = input("Ədəd daxil edin: ")
s = 0
m = 0

for i in n:
    i = int(i)
    if i % 2 == 1:
        s += i
        m += 1
print(s / m)
