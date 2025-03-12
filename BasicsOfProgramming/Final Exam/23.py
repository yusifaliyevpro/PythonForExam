N = 6

x = [(k**2 + 1) // 2 for k in range(N)]
y = [*x, 5, 15, 20]
if sum(y) > 75:
    print(max(y))
else:
    print(min(y))
