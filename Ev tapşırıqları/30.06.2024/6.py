a = [0, 17, 5, 0, 8, 77, 9]

for i in a:
    if i == 0:
        a[a.index(i)] = max(a)
print(a)
