# 10. Count Vowels and Consonants

a = input("Enter the text: ")
vowelsList = ["a", "i", "o", "u", "e"]
vow = 0
con = 0

for i in a:
    if i in vowelsList:
        vow += 1
    elif i.isalpha():
        con += 1
print(f"Vowels: {vow}, Consonants: {con}")
