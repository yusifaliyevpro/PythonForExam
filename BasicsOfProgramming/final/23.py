# 23. The number N is given. The price of the item is entered from TextEdit. 
# When the OK button is clicked, if the entered number is equal to N, 
# the warning window displays 'Yes', otherwise 'No'. Write the program code for this scenario.

N = 15
price = int(input("Enter the price: "))

if price == N:
    print("Yes")
else:
    print("No")