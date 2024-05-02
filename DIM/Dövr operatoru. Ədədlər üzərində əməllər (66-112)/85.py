s = 0

for i in range(1, 201):
    if i % 5 == 0 and i % 3 != 0:
        s += 1
print(s)

# Output: 27
