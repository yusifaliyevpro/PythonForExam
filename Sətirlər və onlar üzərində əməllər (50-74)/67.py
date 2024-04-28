a = [1, 2, 3, 1, 5, 3, 7, 0, 2]
b = []

for i in a:
    if a.count(i) == 1:
        b.append(i)
print(b)

# Output: [5, 7, 0]
