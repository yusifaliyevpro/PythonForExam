a = int(input())
s = 0

for i in str(a):
    s += int(i)

if a % s == 0:
    print("Bölünür")
else:
    print("Bölünmür")

# Input: 2334
# Output: Bölünmür

# Input: 2400
# Output: Bölünür
