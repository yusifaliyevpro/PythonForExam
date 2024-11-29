data = [
    [4169823774525647, 3948, 500],
    [4169823928321928, 9324, 1203],
    [4169823748525438, 9835, 5],
    [5273823723834647, 1928, 40000],
]

lang = int(input("Enter your lang prefence (1: en, 2: az): "))
s = False
if lang == 1:
    opr = int(
        input("What do you want do? (1: show Balance, 2: add, 3: pull, 4: cancel): ")
    )
    cardNumber = int(input("Enter your Card Number: "))
    pin = int(input("Enter your PIN: "))
    for card in data:
        if card[0] == cardNumber and card[1] == pin:
            if opr == 1:
                print(f"You have {card[2]} dollars")
                s = True
            elif opr == 2:
                amount = int(input("How many money do you want to add?: "))
                card[2] += amount
                print(f"You have {card[2]} dollars, now")
            elif opr == 3:
                amount = int(input("How many money do you want to pull?: "))
                card[2] -= amount
                print(f"Take your {amount} dollars")
                print(f"You have {card[2]} dollar, now")
        elif not s:
            print("Your PIN Code or Card Number is wrong")
            break
elif lang == 2:
    opr = int(
        input(
            "Hansı əməliyyatı həyata keçirtmək istəyirsiz? (1: Balansı göstər, 2: Çək, 3: Əlavə et, 4: İmtina et): "
        )
    )
    cardNumber = int(input("Kart nömrənizi daxil edin: "))
    pin = int(input("Pin Kodunuzu daxil edin: "))
    if opr == 1:
        for card in data:
            if card[0] == cardNumber and card[1] == pin:
                print(f"Sizin {card[2]} dollarınız var")
                s = True
        if not s:
            print("PIN kodunuz və ya Kart nömrəniz səhvdir")
else:
    print("Chose a right language prefence")
