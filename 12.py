a = [351, 648, 776, 918]
s = 0

for i in a:
    for j in str(i):
        s += int(j)
print((s-17)*2)
