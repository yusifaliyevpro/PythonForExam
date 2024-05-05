n = int(input("Neçə ədəd daxil edəcəksiz: "))
a = []

for i in range(1, n+1):
    a.append(int(input(f"{i} saylı ədədi daxil edin: ")))

print(max(a))

# Input:
# Neçə ədəd daxil edəcəksiz: 5
# 1 saylı ədədi daxil edin: 2
# 2 saylı ədədi daxil edin: 7
# 3 saylı ədədi daxil edin: 12
# 4 saylı ədədi daxil edin: 465
# 5 saylı ədədi daxil edin: 3

# Output: 465
