N = 12


def f(x):
    a = [k for k in range(1, x, 2)]
    return a


print(sum(f(N // 2 + 1)) + len(f(N - 1)))
