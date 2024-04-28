import math

n = int(input())+1
s = 0

for i in range(0, n):
    s += 1/math.factorial(i)
print(s)

# Input: 10
# Output: 2.7182818011463845

# Input: 100
# Output: 2.7182818284590455

# Input: 1000
# Output: 2.7182818284590455

# Input: 10000
# Output: 2.7182818284590455
