def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Ədəd daxil edin: "))

for i in range(1, n+1):
    print(fibonacci(i))
