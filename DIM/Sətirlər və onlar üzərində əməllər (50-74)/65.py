a = [351, 648, 776, 918]
s = 0

for i in a:
    i = str(i)
    s += int(i[0])+int(i[2])
print(2*s)

# Output: 96
