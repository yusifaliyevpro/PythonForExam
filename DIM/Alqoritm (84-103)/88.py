a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = b**2-4*a*c

if d < 0:
    print("Həlli yoxdur")
elif d == 0:
    print(-b/2*a)
else:
    print((-b-d**0.5)/2*a, (-b+d**0.5)/2*a)
