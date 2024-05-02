n = int(input("n-i daxil edin: "))
s = 0

for i in range(1, n+1):
    s += i*(i+1)*(i+2)
print(s)

# Input: 100
# Output: 26527650
