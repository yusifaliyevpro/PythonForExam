a = [1, 2, 3, 4, 1, 8, 3, 6, 4, 10, 2]
b = []

for i in a:
    if a.count(i) == 1:
        b.append(i)
print(b)

# Output: [8, 6, 10]
