# Verilmiş siyahıda ixtiyarı 8 ədəd daxil edilmişdir
a = [4, 7, 11, 23, 6, 18, 15, 22]

# Cüt ədədlərin cəmini tapan proqram
s = 0
for i in a:
    if i % 2 == 0:
        s += i
print(s)  # Output: 50

# Tək ədədlərin sayını tapan proqram
m = 0

for i in a:
    if i % 2 == 1:
        m += 1
print(m)  # Output: 4

# Tək ədədlərin indexlərini çap edən proqram
for i in a:
    if i % 2 == 1:
        print(a.index(i), end=' ')  # Output: 1 2 3 6
print('\n')

# 3-ə qalıqsız bölünən ədədləri çap edən proqram
for i in a:
    if i % 3 == 0:
        print(i, end=' ')
