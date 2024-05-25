a = float(input("Ədəd daxil edin: "))
b = float(input("Ədəd daxil edin: "))
c = float(input("Ədəd daxil edin: "))

abc = [a, b, c]
abc.sort()
a, b, c = abc

if a**2+b**2 == c**2:
    print("Pifaqor Ədədləridir")
else:
    print("Pifaqor ədəd deyil")
