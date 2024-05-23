# 5. Verilmiş n ədədinin sadə olub olmadığını yoxlayan proqram yazın.

n = int(input("Ədəd daxil edin: "))
m = 0

for i in range(1, n+1):
    if n % i == 0:
        m += 1
if m <= 2:
    print("Sadə ədəddir!")
else:
    print("Sadə ədəd deyil!")
