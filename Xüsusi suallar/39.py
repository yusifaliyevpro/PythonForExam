# 39. İstifadəçidən bir metni daxil etməsini istəyin və metndəki hərflərin sayını və unikal hərflərin sayını hesablayın.

a = input("Mətn daxil edin: ")
s = 0
m = 0

for i in a:
    if i.isalpha():
        s += 1
    if i.isalpha() and a.count(i) == 1:
        m += 1
print(s, m)
