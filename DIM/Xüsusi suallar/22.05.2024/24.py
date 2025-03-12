# 24. İstifadəçidən iki sıyahını (list) qarşılaşdırın və onların bərabər olduğunu yoxlayın.

n = int(input("1-ci Siyahıya neçə element daxil edəcəksiz?: "))
a = []

for i in range(n):
    a.append(input(f"{i+1} saylı elementi daxil edin: "))

m = int(input("2-ci Siyahıya neçə element daxil edəcəksiz?: "))
b = []

for i in range(m):
    b.append(input(f"{i+1} saylı elementi daxil edin: "))

a.sort()
b.sort()

if a == b:
    print("Siyahılar bərabərdir")
else:
    print("Siyahılar bərabər deyil")
