# 23. İstifadəçidən iki sıyahını (list) birləşdirin və birləşdirilmiş sıyahını sort edin.

n = int(input("1-ci Siyahıya neçə element daxil edəcəksiz?: "))
a = []

for i in range(n):
    a.append(input(f"{i+1} saylı elementi daxil edin: "))

m = int(input("2-ci Siyahıya neçə element daxil edəcəksiz?: "))
b = []

for i in range(m):
    b.append(input(f"{i+1} saylı elementi daxil edin: "))

a += b
a.sort()
print(a)
