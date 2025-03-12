# 11. Fibonacci Sequence

n = int(input("Enter a Number: "))
a = 0
b = 1
for i in range(n):
    print(a, b, end=" ")
    a += b
    b += a
