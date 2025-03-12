def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return a * b / gcd(a, b)


print(lcm(5, 7))  # Output: 35.0

# GCD ~ ƏBOB, LCM ~ ƏKOB
