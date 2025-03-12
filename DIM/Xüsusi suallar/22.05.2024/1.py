# 1. Verilmiş n ədədinin amsrtoq ədədi olubolmadığını yoxlayan proqram yazın.

n = input("Ədəd daxil edin: ")
s = 0
for i in n:
    i = int(i)
    s += i**len(n)
if int(n) == s:
    print("Armstrong ədəddir!")
else:
    print("Armstrong ədəd deyil")
