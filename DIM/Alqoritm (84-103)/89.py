n = int(input())
m = 0
s = 0

for i in range(1, n+1):
    m = 1
    for j in range(1, i+1):
        m = m*j
    s = s+m

print(s)
