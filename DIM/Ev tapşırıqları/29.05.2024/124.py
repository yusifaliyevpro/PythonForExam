
for i in range(5000, 10000001):
    s = 0
    for j in str(i):
        j = int(j)
        s += j**len(str(i))
    if s == i:
        print(i)
