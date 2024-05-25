a = [400, 2, 23, 56, 47, 96, 5]
maxx = max(a)

for i in range(len(a)):
    if a[i] % 2 == 0:
        a[i] = maxx
print(a)
