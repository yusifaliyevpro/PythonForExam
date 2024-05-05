n = int(input("Neçə ədəd daxil edəcəksiz: "))
a = []
s = 1
m = 0

for i in range(1, n+1):
    a.append(int(input(f"{i} saylı ədədi daxil edin: ")))

for i in a:
    if i > 0:
        s *= i
for i in a:
    if i < 0:
        m += 1

print(f"Müsbət ədədlərin hasili: {s}")
print(f"Mənfi ədədlərin sayı: {m}")

# Input:
# Neçə ədəd daxil edəcəksiz: 6
# 1 saylı ədədi daxil edin: 3
# 2 saylı ədədi daxil edin: 4
# 3 saylı ədədi daxil edin: 5
# 4 saylı ədədi daxil edin: -2
# 5 saylı ədədi daxil edin: -6
# 6 saylı ədədi daxil edin: -3

# Output:
# Müsbət ədədlərin hasili: 60
# Mənfi ədədlərin sayı: 3
