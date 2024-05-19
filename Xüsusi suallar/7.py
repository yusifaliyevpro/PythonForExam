# 7. Verilmiş n natural ədədinin cüt rəqəmlərinin ədədi ortasını hesablayan proqram yazın.

n = input("Ədəd daxil edin: ")
s = 0
m = 0

for i in n:
    i = int(i)
    if i % 2 == 0:
        s += i
        m += 1
print(s / m)
