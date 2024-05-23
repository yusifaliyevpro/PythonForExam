# 25. Klaviaturadan daxil edilmiş rəqəmlərdən ibarət olan bir sətrin 3-cü, 7-ci və 9-cu indekslərində “4” yerləşdir. Bu sətrin “4” olan hissələrindən bölünərək yeni bir siyahı yaradan proqramı yazın.

a = input("Mətn daxil edin: ")
m = 0
s = ''

for i in a:
    if m in [3, 7, 9]:
        s += "4"
    else:
        s += i
    m += 1

print(s.split('4'))
