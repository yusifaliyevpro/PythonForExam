# 12. Verilmiş natural ədədin cüt rəqəmlərini cəmləyən proqram yazın.

n = input("Ədəd daxil edin: ")
s = 0

for i in n:
    i = int(i)
    if i % 2 == 0:
        s += i
print(s)
