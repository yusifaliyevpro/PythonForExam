n = int(input("Neçə ədəd daxil edəcəksiz: "))
a = []
s = 0
m = 0

for i in range(1, n+1):
    a.append(int(input(f"{i} saylı ədədi daxil edin: ")))

for i in a:
    if i < 0:
        s += i
        m += 1
print(s/m)

# Input:
# Neçə ədəd daxil edəcəksiz: 5
# 1 saylı ədədi daxil edin: 2
# 2 saylı ədədi daxil edin: -3
# 3 saylı ədədi daxil edin: -4
# 4 saylı ədədi daxil edin: -5
# 5 saylı ədədi daxil edin: -6

# Output: -4.5
