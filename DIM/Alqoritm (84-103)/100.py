n = int(input())
x = int(input())
s = 0

for i in range(1, n+1):
    s += (n-1)*x+n
print(s)
