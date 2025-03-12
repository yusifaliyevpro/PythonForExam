# Daxil edilmiş 3 ədədin pifaroq ədəd olduğunu müəyyən edən proqram yazın

a = []
for i in range(1, 4):
    a.append(float(input(f"{i} saylı ədədi daxil edin: ")))
a.sort()
a, b, c = a

if a**2+b**2 == c**2:
    print("Pifaqor Ədədlərdir")
else:
    print("Pifaqor Ədədlər deyil")

# Input:
# 1 saylı ədədi daxil edin: 3
# 2 saylı ədədi daxil edin: 4
# 3 saylı ədədi daxil edin: 5

# Output: Pifaqor Ədədlərdir
