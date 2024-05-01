n = int(input())
a = []

m = 2
while n > 1:
    if n % m == 0:
        a.append(m)
        n = n//m
    else:
        m += 1

for i in a:
    print(i)

# Input: 845
# Output:
# 5
# 13
# 13
