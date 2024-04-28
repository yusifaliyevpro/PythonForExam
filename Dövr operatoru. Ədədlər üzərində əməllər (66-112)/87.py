import math

a = int(input("Ədəd daxil edin: "))

if a % 2 == 0:
    print(math.factorial(a))
else:
    print(a**2*2)

# Input: 5
# Output: 50

# Input: 6
# Output: 720
