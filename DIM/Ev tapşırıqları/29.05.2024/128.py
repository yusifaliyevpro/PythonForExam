a = [400, 2, 23, 56, 47, 96, 5]
minn = min(a)

for i in range(len(a)):
    if a[i] % 2 == 1:
        a[i] = minn
print(a)
