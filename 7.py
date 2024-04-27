y = []
m = 0

for x in range(-10, 11):
    if x > 3:
        y.append(x**2-5*x+6)
    else:
        y.append((x+2)**2)

for i in y:
    if i % 3 == 0:
        m += 1
print(m)
