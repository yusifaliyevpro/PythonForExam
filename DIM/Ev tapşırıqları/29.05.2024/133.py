s = input("Mətn daxil edin: ").split(" ")
a = []

for i in s:
    a.append(i.count("a"))
print(s[a.index(max(a))])
