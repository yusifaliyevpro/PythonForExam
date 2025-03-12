# 70. Climbing Stairs

n = int(input("Enter number: "))


def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(n + 1))
