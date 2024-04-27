a = [12, 45, 23, 16, 121, 34, 66, 15]
s = 0

for i in a:
    if str(i).count('1') > 0:
        s += 1
print(s)
