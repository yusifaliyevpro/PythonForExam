n = int(input("Ədəd daxil edin: "))
a = []

for i in range(1, n+1):
    if n % i == 0:
        a.append(i)
print(a)

# Input: 100
# Output: [1, 2, 4, 5, 10, 20, 25, 50, 100]
