N = 16


def f(i, x):
    a = [k for k in range(i, x, 2)]
    return a


print(sum(f(1, N // 2)) + sum(f(2, N)))
