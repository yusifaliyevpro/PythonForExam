x = float(input())
y = 0

if x < 0:
    y += 2*x**2+3*x
elif x == 0:
    y += 5*x+4
else:
    y += x**3-4
print(y)
