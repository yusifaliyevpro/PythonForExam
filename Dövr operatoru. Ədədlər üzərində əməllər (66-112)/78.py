n = int(input("Sayı daxil edin: "))
k = []
m = []

for i in range(1, n+1):
    a = int(input(f"{i} saylı ədədi daxil edin: "))
    if a % 2 == 1:
        k.append(a)
    else:
        m.append(a)
print(m, k)

# Input:
# Sayı daxil edin: 4
# 1 saylı ədədi daxil edin: 56
# 2 saylı ədədi daxil edin: 25
# 3 saylı ədədi daxil edin: 13
# 4 saylı ədədi daxil edin: 42

# Output:
# [56, 42] [25, 13]
