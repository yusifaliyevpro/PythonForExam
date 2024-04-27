a = input()
s = 0

for i in a:
    if a.count(i) == 1:
        s += 1
print(s)
