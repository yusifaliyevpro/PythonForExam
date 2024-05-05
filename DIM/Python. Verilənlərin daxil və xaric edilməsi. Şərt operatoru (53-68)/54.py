a = []

for i in range(1, 4):
    a.append(float(input(f"{i} saylı ədədi daxil edin: ")))
a, b, c = a

if a == b == c:
    print("Bərabərtərəflidir")
elif a != b != c:
    print("Müxtəliftərəflidir")
else:
    print("Bərabəryanlıdır")

# Input:
# 1 saylı ədədi daxil edin: 5
# 2 saylı ədədi daxil edin: 5
# 3 saylı ədədi daxil edin: 5
# Output: Bərabərtərəflidir

# Input:
# 1 saylı ədədi daxil edin: 5
# 2 saylı ədədi daxil edin: 5
# 3 saylı ədədi daxil edin: 7
# Output: Bərabəryanlıdır

# Input:
# 1 saylı ədədi daxil edin: 2
# 2 saylı ədədi daxil edin: 7
# 3 saylı ədədi daxil edin: 9
# Output: Müxtəliftərəflidir
