n = int(input("Ədəd daxil edin: "))
s = 0

for i in range(1, n+1):
    if n % i == 0:
        s += 1
print(s)

# Input: 100
# Output: 9
