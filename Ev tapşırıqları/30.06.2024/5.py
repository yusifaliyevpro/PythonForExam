a = [6, 28, -24, 7, 12, 99, 66, 100]

for i in range(0, len(a)):
    if a[i] % 3 == 0 and a[i] % 4 == 0:
        print(a[i], i)
