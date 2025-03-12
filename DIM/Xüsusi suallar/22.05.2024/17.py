# 17. İstifadəçidən bir rəqəmin faktorialını hesablayan bir proqram yazın.

n = int(input("Ədəd daxil edin: "))


def fact(n):
    m = 1
    for i in range(1, n+1):
        m *= i
    return m


print(fact(n))

# from math import factorial

# print(factorial(n))
