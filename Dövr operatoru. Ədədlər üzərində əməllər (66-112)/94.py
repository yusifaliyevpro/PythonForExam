a = list(input("16-lıq say sistemində ədəd daxil edin: "))
a.reverse()
m = 0
s = 0
for i in a:
    if i.isdigit():
        s += int(i)*16**m
    elif i == "A":
        s += 10*16**m
    elif i == "B":
        s += 11*16**m
    elif i == "C":
        s += 12*16**m
    elif i == "D":
        s += 13*16**m
    elif i == "E":
        s += 14*16**m
    elif i == "F":
        s += 15*16**m
    m += 1
print(s)

# Input: AA
# Output: 170
