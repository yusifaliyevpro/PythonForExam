# Klaviaturadanz 0 daxil edilənə qədər daxil edilmiş rəqəmlərin cəmini tapan proqram yazın

a = []
n = int(input("Neçə ədəd daxil edəcəksiz?: "))
s = 0

for i in range(1, n+1):
    a.append(float(input(f"{i} saylı ədədi daxil edin: ")))

for i in a:
    if i == 0:
        break
    else:
        s += i
print(s)

# Input:
# Neçə ədəd daxil edəcəksiz?: 5
# 1 saylı ədədi daxil edin: 2
# 2 saylı ədədi daxil edin: 11
# 3 saylı ədədi daxil edin: 7
# 4 saylı ədədi daxil edin: 0
# 5 saylı ədədi daxil edin: 5

# Output: 20.0
