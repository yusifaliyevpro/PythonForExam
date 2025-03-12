# 1-dən n-ə kimi ədədlərin hasilini tapın (def ilə)
from math import factorial


def fact(n):
    return factorial(n)


n = int(input("Ədəd daxil edin: "))
print(fact(n))

# Input: 5
# Output: 120
