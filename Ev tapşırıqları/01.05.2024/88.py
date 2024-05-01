a = []

for i in range(1, 4):
    a.append(float(input(f"{i} saylı ədədi daxil edin: ")))
a.sort()
a, b, c = a

if not b-a < c < a+b:
    print("Üçbucağın tərəfləri ola bilməz!")
elif a == b == c:
    print("Üç tərəfi bərabərdir")
elif a != b != c:
    print("Üçbucağın bütün tərəfləri fərqlidir")
else:
    print("İki tərəfi bərabərdir")

# Input:
# 1 saylı ədədi daxil edin: 5
# 2 saylı ədədi daxil edin: 6
# 3 saylı ədədi daxil edin: 7

# Output: fərqlidir
