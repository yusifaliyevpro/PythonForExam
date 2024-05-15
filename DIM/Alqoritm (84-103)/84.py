a = float(input("1: "))
b = float(input("2: "))

if a > b:
    a -= b
    print(a)
elif b > a:
    b -= a
    print(b)
else:
    print("Daxil etdiyiniz rəqəmlər bərabərdir. Cavab sıfıra bərabər olacaq")
