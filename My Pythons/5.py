n = int(input("Ədəd daxil edin: "))
a = [n]
while n != 1:
    if n % 2 == 0:
        n = n//2
    else:
        n = 3*n+1
    a.append(n)
print(a)
