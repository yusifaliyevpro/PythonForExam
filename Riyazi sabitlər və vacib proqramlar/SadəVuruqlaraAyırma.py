k = []
d = []
for x in range(2, 100, 2):
    d.append(x)
    for i in range(len(d)-1):
        if (d[i]+d[i+1]) % 6 == 0:
            k.append(str(d[i])+str(d[i+1]))
print(k)
