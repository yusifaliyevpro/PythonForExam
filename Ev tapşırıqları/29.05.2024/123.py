
for i in range(1000, 5001):
    s = 0
    for j in str(i):
        j = int(j)
        s += j**4
    if s == i:
        print(i)
