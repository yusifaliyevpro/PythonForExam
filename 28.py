a = input("Sətiri daxil edin: ")
s = 0

for i in a:
    if i.isdigit():
        s += int(i)
print(s)
