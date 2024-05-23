# 32. İstifadəçidən bir metni daxil etməsini istəyin və bu metndəki ən uzun və ən qısa sözləri tapın və nəticəni çap edin. (sözlər bir boşluqla ayrılıb, eyni uzunluqda söz yoxdur)

a = input("Mətn daxil edin: ").split()
b = []

for i in a:
    b.append(len(i))

print(a[b.index(max(b))])
print(a[b.index(min(b))])
