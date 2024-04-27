x = [13, 27, 19, 23]
y = []
s = 0

for i in x:
    for j in str(i):
        s += int(j)
    y.append(s)
    s = 0
print(y)
