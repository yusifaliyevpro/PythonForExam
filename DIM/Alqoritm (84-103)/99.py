a = []
s = 0

for i in range(1, 11):
    a.append(float(input(f"{i} saylı ədədi daxil edin: ")))

for i in a:
    if i % 2 == 0:
        s += i

print(s)
