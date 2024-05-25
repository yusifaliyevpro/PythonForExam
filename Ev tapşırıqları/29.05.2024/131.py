n = int(input("Ədəd daxil edin: "))
a = []

while n != 1:
    for i in range(2, n+1):
        if n % i == 0:
            n = n//i
            a.append(i)
            break
print(a)
