# 1. Basic Arithmetic Calculator


opr = ""
while opr != "q":
    a = int(input("Enter variable a: "))
    b = int(input("Enter variable b: "))
    opr = input("Enter Opr (+, -, *, /, q-Quit): ")

    if opr == "+":
        print(a + b)
    elif opr == "-":
        print(a - b)
    elif opr == "*":
        print(a * b)
    elif opr == "/":
        print(a / b)
    else:
        print("You entered a wrong operation. Try Again")
print("Thank you for using my calculator!")
