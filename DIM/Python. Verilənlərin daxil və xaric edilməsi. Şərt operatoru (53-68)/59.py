a = float(input("a-nı daxil edin: "))
b = float(input("b-ni daxil edin: "))

if a < b:
    print(3*b/abs(a-b)+3*(a+b))
elif a == b:
    print((2*a**2+abs(b**3))**0.5)
else:
    print(a**2/abs(a+b))

# Input:
# a-nı daxil edin: 6
# b-ni daxil edin: 10

# Output: 55.5
