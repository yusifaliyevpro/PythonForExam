a = int(input(("First Value: ")))
b = int(input(("Second Value: ")))
opr = input("Operation (+,-,*,/,C): ")


if opr == "+":
    print(a + b)
elif opr == "*":
    print(a * b)
elif opr == "/":
    print(a / b)
elif opr == "-":
    print(a - b)
else:
    print("Error. Please Input a write operation")

while True:
    a = int(input(("First Value: ")))
    b = int(input(("Second Value: ")))
    opr = input("Operation (+,-,*,/,C): ")
