n = int(input("Neçə rəqəm daxil edəcəksiz?: "))
a = []

for i in range(0, n):
    a.append(int(input(f"{i+1} saylı rəqəmi daxil edin: ")))

print(sum(a)/len(a))

# Input:
# Neçə rəqəm daxil edəcəksiz?: 4
# 1 saylı rəqəmi daxil edin: 1
# 2 saylı rəqəmi daxil edin: 8
# 3 saylı rəqəmi daxil edin: 3
# 4 saylı rəqəmi daxil edin: 6

# Output: 4.5
