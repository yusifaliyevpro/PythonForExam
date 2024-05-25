n = int(input("Bir ədəd daxil edin: "))
s = 0

for i in range(2, n):
    if int(n/i) == n/i:
        s += 1

if s > 1:
    print("Mürəkkəb ədəddir")
else:
    print("Sadə ədəddir")
