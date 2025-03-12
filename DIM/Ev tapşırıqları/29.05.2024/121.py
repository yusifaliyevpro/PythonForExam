n = int(input("Ədəd daxil edin: "))
s = 0
for i in str(n):
    i = int(i)
    s += i**3
if s == n:
    print("Armstrong Ədəddir")
else:
    print("Armstrong Ədəd deyil")
