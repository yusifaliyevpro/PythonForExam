# 35. İstifadəçidən bir metni daxil etməsini istəyin və bu metndəki unikal (təkrarlanmayan) sözləri tapın. (sözlər bir boşluqla ayrılıb)

a = input("Mətn daxil edin: ").split()

for i in a:
    if a.count(i) == 1:
        print(i)
