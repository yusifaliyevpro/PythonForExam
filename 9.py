a = [13, 27, 19, 23]
y = []
s = 0

for i in a:
    for j in str(i):
        s += int(j)
    y.append(s)
    s = 0
print(y)  # Output: [4, 9, 10, 5]
