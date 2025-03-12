a = input("Enter the list (with space): ")
a = list(map(int, a.split()))
a.sort()
a, b, c = a

if a**2 + b**2 == c**2:
    print("It is Pifragorian ")
else:
    print("It is not")

# Input:
# 1 saylı ədədi daxil edin: 12
# 2 saylı ədədi daxil edin: 5
# 3 saylı ədədi daxil edin: 13

# Output: Pifaqor ədədləridir
