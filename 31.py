a = input("Ədəd daxil edin: ")
b = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

for i in a:
    if b.count(i) > 0:
        b.remove(i)
print(b, len(b))
