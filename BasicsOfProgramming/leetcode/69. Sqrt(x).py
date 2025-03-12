# 69. Sqrt(x)

n = int(input("Enter number: "))
i = 1

while i <= n:
    if i * i == n:
        print(i)
        break
    elif i * i > n:
        print(i - 1)
        break
    i += 1
