# ƏBOB-un tapılması üçün proqram
# Euclid-in alqoritmindən istifadə edək

x = int(input("İlk ədədi daxil edin: "))
y = int(input("İkinci ədədi daxil edin: "))

print(f"ƏBOB({x}; {y})", end=' = ')

while x != y:
    if x > y:
        x -= y
    else:
        y -= x
print(x)

# Input:
# 15
# 35
# Output: 5


# Əslində biz bunu aşağıdaki kimi python-un öz imkanları ilədə rahat və asan yolla edə bilərik.
# Lakin ola bilər xüsusi qayda qoyulsun ki, dövrdən istifadə etmək mütləqdir. Bu zaman yuxarıdaki proqram keçərlidir

# import math
# print(math.gcd(x, y))
