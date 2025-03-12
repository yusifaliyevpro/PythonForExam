a1 = int(input("Ilk həddi: "))
d = int(input("Silsilə vuruğu: "))
n = int(input("Ədəd daxil edin: "))
m = []

for i in range(1, n+1):
    m.append(a1+d*(i-1))
print(m)

# Input:
# Ilk həddi: 5
# Silsilə vuruğu: 5
# Ədəd daxil edin: 5

# Output: [5, 10, 15, 20, 25]
