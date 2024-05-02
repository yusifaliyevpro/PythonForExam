a = [123, 4532, 3431, 2345, 67864]
b = []

for i in a:
    i = str(i)
    b.append(int(i[::-1]))
print(b)

# Output: [321, 2354, 1343, 5432, 46876]
