y = 0
m = 0
for x in range(-10, 11):
    if x > 3:
        y = x**2-5*x+6
    else:
        y = (x+2)**2
    if y % 3 == 0:
        m += 1
print(m)

# Output: 8
