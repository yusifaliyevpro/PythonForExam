a = int(input("Ədəd daxil edin: "))
b = int(input("Ədəd daxil edin: "))


def IsSadə(n):
    s = 0
    for i in range(2, n):
        if n % i == 0:
            return True


for i in range(a, b + 1):
    if IsSadə(i):
        print(i)
