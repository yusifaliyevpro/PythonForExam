# 6. Sum of Digits


# Method 1
def sumDigits(n):
    s = 0
    while n != 0:
        s += n % 10
        n = n // 10
    return s


# Method 2
def sumDigits(n):
    n = list(map(int, str(n)))
    return sum(n)
