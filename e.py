import math

n = int(input())+1
s = 0

for i in range(0, n):
    s += 1/math.factorial(i)
print(s)
