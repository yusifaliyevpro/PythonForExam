N = 12

x = [k for k in range(N)]
y = [k for k in x if k % 2 != 0]
print(y)
if len(y) < 6:
    print(sorted(y))
else:
    z = sorted(y, reverse=True)
    print(z)
