# Armstrong numbers

n = int(input("Ədəd daxil edin: "))
a = []

for i in range(1, n+1):
    m = len(str(i))
    s = 0
    for j in str(i):
        j = int(j)
        s += j**m
    if i == s:
        a.append(i)
print(a)

# Input: 10000
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474]
