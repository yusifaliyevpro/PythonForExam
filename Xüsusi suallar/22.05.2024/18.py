# 18. İstifadəçidən bir sıyahı (list) və bir element daxil etməsini istəyin və bu elementin sıyahının içində olub olmadığını yoxlayın.

n = int(input("Siyahıya neçə ədəd daxil edəcəksiz?: "))
a = []

for i in range(1, n+1):
    a.append(input(f"{i} saylı elementi daxil edin: "))

c = input("Yoxlamaq istədiyiniz elementi qeyd edin: ")

if c in a:
    print("Daxil etdiyiniz element siyahıda var!")
else:
    print("Daxil etdiyiniz element siyahıda yoxdur!")
