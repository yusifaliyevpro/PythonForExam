# GREGORY/LEIBNIZ Formula
n = int(input("Hədd sayı: ")) + 1
s = 0

for i in range(0, n):
    s += ((-1) ** i) / (2 * i + 1)
print(4 * s)

# Input: 10
# Output: 3.232315809405594

# Input: 100
# Output: 3.1514934010709914

# Input: 1000
# Output: 3.1425916543395442

# Input: 10000
# Output: 3.1416926435905346

# Input: 100000000
# Output: 3.141592663589326
