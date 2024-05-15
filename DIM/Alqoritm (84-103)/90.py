n = int(input("Neçə ədəd daxil edəcəksiz?: "))
a = []

for i in range(1, n+1):
    a.append(float(input(f"{i} saylı ədədi daxil edin: ")))

print(sum(a)/n)
