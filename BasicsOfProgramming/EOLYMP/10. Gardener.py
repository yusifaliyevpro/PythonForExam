# 10. Gardener
n = int(input())
m = 0
s = 0.0

for i in range(n, 0, -1):
    s += 1.0 / i
    if s > 0.5:
        break
    m += 1

print(n - m)
