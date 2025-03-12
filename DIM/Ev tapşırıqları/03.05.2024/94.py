# a ədədi ilə b ədədinin ƏBOB-unun tapılması üçün proqram yazın (def ilə)
from math import gcd


def EBOB(a, b):
    return gcd(a, b)


a = int(input("a: "))
b = int(input("b: "))
print(EBOB(a, b))

# Input:
# a: 15
# b: 35

# Output: 5
