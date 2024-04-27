a = input("Ingilis Əlifbasındakı hərflərdən ibarət cümlə daxil edin: ")
c = ""

for i in a:
    if i == 'a':
        c += 'b'
    elif i == 'b':
        c += 'a'
    else:
        c += i
print(c)
