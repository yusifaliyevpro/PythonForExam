a = int(input("Doğduğunuz ayı daxil edin: "))

b = [[12, 1, 2], "Qış", [3, 4, 5], "Yaz",
     [6, 7, 8], "Yay", [9, 10, 11], "Payız"]

for i in range(0, 8, 2):
    if a in b[i]:
        print(f"Sizin ad gününüz {b[i+1]}dadır")
    else:
        print("Daxil etdiyiniz rəqəm 1-12 intervalında olmalıdır")

# Input: 9
# Output: Sizin ad gününüz Payızdadır
