# Armstrong numbers

a = int(input("Ədəd daxil edin: "))
b = int(input("Ədəd daxil edin: "))


for i in range(a, b + 1):
    m = len(str(i))
    s = 0
    for j in str(i):
        j = int(j)
        s += j**m
    if i == s:
        print(i)

# Input: 10000
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474]
