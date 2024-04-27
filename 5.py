a = [3, 4, 2, 1, 6, 9, 7, 8, 12, 10, 5, 14]
s = 0
m = 0

for i in range(0, len(a)):
    if ((i % 2 == 1 and a[i] % 2 == 0) or (i % 2 == 0 and a[i] % 2 == 1)) and i != 0:
        s += a[i]
        m += 1
print(s//m)
