a = [3, 4, 2, 1, 6, 9, 7, 8, 12, 10, 5, 14]
b = []
s = 0

for i in a:
    if (a.index(i) % 2 == 1 and i % 2 == 0) or (a.index(i) % 2 == 0 and i % 2 == 1):
        b.append(i)
print(sum(b)/len(b))

# Output: 7.285714285714286
