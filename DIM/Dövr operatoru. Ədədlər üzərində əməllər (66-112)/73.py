n = int(input("Sayı daxil edin: "))+1
a = []

for i in range(1, n):
    a.append(int(input(f"{i} saylı ədədi daxil edin: ")))

print(max(a))

# Input:
# Sayı daxil edin: 5
# 1 saylı ədədi daxil edin: 3
# 2 saylı ədədi daxil edin: 62
# 3 saylı ədədi daxil edin: 1
# 4 saylı ədədi daxil edin: 5
# 5 saylı ədədi daxil edin: 7

# Output: 62
