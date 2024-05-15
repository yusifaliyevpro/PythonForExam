l = int(input("Neçə ədəd daxil edəcəksiz?: "))
a = []
s = 0
m = 0

for i in range(1, l+1):
    a.append(float(input(f"{i} saylı ədədi daxil edin: ")))

for i in a:
    if i > 0:
        s += i
    elif i < 0:
        m += 1
print(s, m)
