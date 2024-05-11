# 1. (Asan olan): Verilmiş a = [5, 20, 15, 90, 75, 37, 29, 80, 29, 45] siyahısındaki elementlərdən həm 3-ə həm 5-ə bölünən, amma 10-a bölüməyənləri ekrana çap edən proqram yazın

for i in a:
    if i % 3 == 0 and i % 5 == 0 and i % 10 != 0:
        print(i)
