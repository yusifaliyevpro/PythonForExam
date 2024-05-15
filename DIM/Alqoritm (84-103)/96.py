m = int(input())
a = []

for i in range(1, m+1):
    a.append(float(input(f"{i} saylı ədədi daxil edin: ")))
print(sum(a))
