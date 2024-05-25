
for i in range(100, 501):
    s = 0
    for j in str(i):
        j = int(j)
        s += j**3
    if s == i:
        print(i)
