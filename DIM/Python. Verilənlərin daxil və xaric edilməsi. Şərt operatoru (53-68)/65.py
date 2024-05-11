a = ["Qış", "Yaz", "Yay", "Payız"]
n = int(input("Ayın nömrəsini daxil edin: "))

if n in [12, 1, 2]:
    print(a[0])
elif n in [3, 4, 5]:
    print(a[1])
elif n in [6, 7, 8]:
    print(a[2])
elif n in [9, 10, 11]:
    print(a[3])
else:
    print("Ayın nömrəsini düzgün daxil edin!!!")

# Input: 12
# Output: Qış

# Input: 5
# Output: Yaz
