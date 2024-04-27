a = input("Cümlə daxil edin: ")
s = ""

for i in a:
    if not i.isdigit():
        s += i
print(s)
