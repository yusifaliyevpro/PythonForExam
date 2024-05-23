# 29. Üç ədədin tək olanlarını çap edən proqram yazın.

a = int(input("Ədəd daxil edin: "))
b = int(input("Ədəd daxil edin: "))
c = int(input("Ədəd daxil edin: "))

for i in [a, b, c]:
    if i % 2 == 1:
        print(i)
