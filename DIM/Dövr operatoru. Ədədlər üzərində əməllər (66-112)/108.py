def check(a):
    m = 0
    for i in a:
        i = int(i)
        if i >= 8:
            m += 1
    if m == 0:
        return "Mövcuddur"
    else:
        return "Mövcud deyil"


a = input("Ədəd daxil edin: ")
print(check(a))

# Input: 157
# Output: Mövcuddur

# Input: 298
# Output: Mövcud deyil
