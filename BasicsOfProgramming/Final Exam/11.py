N = 6

x = [k for k in range(N)]
if N >= 5:
    x.reverse()
else:
    x = 2 * [*x, 10, 15]
print(x)
