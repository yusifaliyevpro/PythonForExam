from math import factorial
n = int(input())
s = 0

for i in range(1, n+1):
    s += 1/factorial(i)
print(s)
