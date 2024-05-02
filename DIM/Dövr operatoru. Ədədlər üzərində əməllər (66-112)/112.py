a = int(input("Çox rəqəmli natural ədədi daxil edin: "))
n = 0


def getCem(a):
    a = str(a)
    return int(a[0])+int(a[-1])


while a > 0:
    a -= getCem(a)
    n += 1
print(n)

# Input: 595
# Output: 60

# Input: 214
# Output: 22
