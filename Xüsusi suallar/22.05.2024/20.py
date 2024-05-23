# 20. İstifadəçidən iki ədəd daxil etməsini istəyin və bu ədədlərin ən böyük ortaq böləni tapın.

x = int(input("İlk ədədi daxil edin: "))
y = int(input("İkinci ədədi daxil edin: "))

print(f"ƏBOB({x}; {y})", end=' = ')

while x != y:
    if x > y:
        x -= y
    else:
        y -= x
print(x)
