from math import factorial
x = float(input("x-i daxil edin: "))
n = int(input("n-i daxil edin: "))
s = 0

for i in range(1, n+1):
    s += (-1)**(i+1)*x**i/factorial(i)
print(s)

# Input:
# x-i daxil edin: 5
# n-i daxil edin: 100

# Output: 0.9932620530009132
