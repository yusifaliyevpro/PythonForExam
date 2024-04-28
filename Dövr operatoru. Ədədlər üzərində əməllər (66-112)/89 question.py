n = int(input("Ədəd daxil edin: "))
s = 0


def factorial(x):
    m = 1
    for i in range(1, x+1):
        m *= i
    return m


for i in range(1, n+1):
    s += (-1)**i/factorial(i)**i
print(s)
