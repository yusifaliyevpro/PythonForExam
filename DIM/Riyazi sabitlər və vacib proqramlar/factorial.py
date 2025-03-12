def factorial(x):
    m = 1
    for i in range(1, x+1):
        m *= i
    return m


print(factorial(5))
