# + Bonus Müəllim üçün sual: Ulduz rəqəmlərindən içərisində olan 37 rəqəminin bu siyahının neçənci elementi olduğunu, və klaviaturadan daxil edilmiş ədədin 1000-dən kiçik natural ədədin ulduz rəqəmi olub-olmadıını çap edən proqram yazın. Ulduz rəqəmlərinin nə olduğu haqqında internetdən araşdıra və hesablama formulunu əldə edə bilərsiz.

stars = []
n = int(input("Ədəd daxil edin: "))

for i in range(1, 10):
    stars.append(6*i*(i-1)+1)

print(stars.index(37)+1)  # 37-nin neçənci hədd olduğunu çap edir
print(stars)  # Siyahını çap edir

if stars.count(n) != 0:
    print("Ulduz Ədədidir")
else:
    print("Ulduz ədədi deyil")

# Output:
# 3
# [1, 13, 37, 73, 121, 181, 253, 337, 433]
# Ulduz Ədədidir
