a = []
for i in range(1, 4):
    a.append(int(input(f"{i} saylı ədədi daxil edin: ")))
a.sort()
a, b, c = a

if a**2+b**2 == c**2:
    print("Pifaqor ədədləridir")
else:
    print("Pifaqor ədədləri deyil")

# Input:
# 1 saylı ədədi daxil edin: 12
# 2 saylı ədədi daxil edin: 5
# 3 saylı ədədi daxil edin: 13

# Output: Pifaqor ədədləridir
