N = 3


def mixed_f(a, b=1, c=2):
    z = a + b**2 + c**3
    return z


print(mixed_f(N) * mixed_f(N - 1))
