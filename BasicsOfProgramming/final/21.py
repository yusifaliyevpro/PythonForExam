# 21. The number N is given. A number is selected from the spinner. 
# When the OK button is clicked, if the number in the spinner is greater than N, 
# the warning window displays 'Yes', otherwise 'No'. Write the program code for this scenario.

N = 5
spinner_value = int(input("Enter a number from spinner: "))

if spinner_value > N:
    print("Yes")
else:
    print("No")