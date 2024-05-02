m = int(input("Rəqəmləri hasilini daxil edin: "))


for i in range(100, 1000):
    a = i//100
    b = (i//10) % 10
    c = i % 10
    if a*b*c == m and a != 1 and b != 1 and c != 1:
        print(i)

# Input: 20
# Output:
# 225
# 252
# 522
