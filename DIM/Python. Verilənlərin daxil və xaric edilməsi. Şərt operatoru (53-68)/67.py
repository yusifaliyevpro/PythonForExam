n = int(input("n-i daxil edin: "))
b = int(input("b-ni daxil edin (b!=0): "))
m = 0

for i in range(1, n):
    if i**2 % b == 0:
        m += 1
print(m)

# Input:
# n-i daxil edin: 50
# b-ni daxil edin (b!=0): 3

# Output: 16
