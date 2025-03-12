b1 = int(input("Ilk həddi: "))
q = int(input("Silsilə vuruğu: "))
n = int(input("Ədəd daxil edin: "))
m = []

for i in range(1, n+1):
    m.append(b1*q**(i-1))
print(m)

# Input:
# Ilk həddi: 2
# Silsilə vuruğu: 2
# Ədəd daxil edin: 5

# Output: [2, 4, 8, 16, 32]
