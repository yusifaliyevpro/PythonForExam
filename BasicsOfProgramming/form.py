attempts = 1
answer = input("Enter this (2x^3-5)/3y^2 + (xy+5y+2)/9 equation as a python equation: ")
trueArithmetic = [
    "(2*x**3-5)/(3*y**2)+(x*y+5*y+2)/9",
    "(2*x*x*x-5)/(3*y*y)+(x*y+5*y+2)/9",
]
answer.replace(" ", "", -1)
while not (answer in trueArithmetic):
    if answer == "Quit" or answer == "show":
        break
    elif answer == "":
        pass
    else:
        print("It is wrong!. Please try again")
        attempts += 1
    answer = input(
        "Enter this (2x^3-5)/(3y^2) + (xy+5y+2)/9 equation as a python equation: "
    )

print("Number of attempts: ", attempts)
if (
    answer != "Quit"
    and answer != ""
    and answer == "show"
    and not answer in trueArithmetic
):
    print(
        "You could write it as like this: ",
        trueArithmetic[0],
        " or ",
        trueArithmetic[1],
    )
