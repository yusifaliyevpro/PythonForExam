a = []
for i in range(1, 4):
    a.append(int(input(f"{i} saylı ədədi daxil edin: ")))
a.sort()

if a[0]**2+a[1]**2 == a[2]**2:
    print("Pifaqor ədədləridir")
else:
    print("Pifaqor ədədləri deyil")

# Input:
# 1 saylı ədədi daxil edin: 12
# 2 saylı ədədi daxil edin: 5
# 3 saylı ədədi daxil edin: 13y

# Output: Pifaqor ədədləridir
