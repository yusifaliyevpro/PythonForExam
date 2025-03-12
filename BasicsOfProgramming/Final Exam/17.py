N = 8


def f(x):
    a = [k for k in range(x)]
    return a


print(sum(f(N // 2)) + len(f(N)))
