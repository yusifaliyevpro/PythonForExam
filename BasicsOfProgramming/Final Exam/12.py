N = 8

x = [k for k in range(N)]
y = [k for k in x if k % 2 != 1]
if len(y) < 5:
    print(sum(y))
else:
    print(y[-1])
