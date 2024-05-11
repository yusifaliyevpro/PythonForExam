a = []
for i in range(1, 4):
    a.append(int(input(f"{i} saylı ədədi daxil edin: ")))
a.sort()

print(f"Qiymətcə orta olan = {a[1]}")

# Input:
# 1 saylı ədədi daxil edin: 5
# 2 saylı ədədi daxil edin: 8
# 3 saylı ədədi daxil edin: 2

# Output: Qiymətcə orta olan 5
