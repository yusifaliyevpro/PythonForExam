# 36. İstifadəçidən bir metni daxil etməsini istəyin və bu metni hərflərin sayını hesablayaraq çap edin.

a = input("Mətn daxil edin: ")
s = 0

for i in a:
    if i.isalpha():
        s += 1
print(s)
