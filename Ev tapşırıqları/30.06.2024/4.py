a = input("Mətn daxil edin: ")
s = ""

for i in a:
    if (not i.isspace()) and (s.count(i) == 0 or a.count(i) == 1):
        s += i
print(s)
