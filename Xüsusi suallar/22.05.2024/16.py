# 16. İstifadəçidən bir rəqəmi daxil etməsini istəyin və bu rəqəmi sıfıra qədər olan bütün ədədlərlə bölün.

n = int(input("Ədəd daxil edin: "))

for i in range(1, n+1):
    n = n/i
print(n)
