a = [2314, 342, 1206, 4321, 57, 78965]
b = []

for i in a:
    b.append((int(max(str(i))))**2 + (int(min(str(i))))**2)

print(b)

# Output: [17, 20, 36, 17, 74, 106]
