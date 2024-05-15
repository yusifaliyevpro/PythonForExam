from math import factorial
x = int(input("x: "))
n = int(input("n: "))
p = 0

for i in range(1, n+1):
    p += x**i/factorial(i)
print(p)
