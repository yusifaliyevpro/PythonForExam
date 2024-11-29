# 13. Temperature Converter

opr = input("Enter the operation to (f or c): ")
temp = float(input("Enter the Temprature: "))
if opr == "f":
    print((temp * 9 / 5) + 32)
elif opr == "c":
    print((temp - 32) * 9 / 5)
else:
    print("You entered a wrong opreation")
