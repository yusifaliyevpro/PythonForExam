a = input("Ədəd daxil edin: ")
b = []

for i in a:
    i = int(i)
    if i % 2 == 1:
        b.append(i)
if b != []:
    print(min(b))
else:
    print("Tək ədəd yoxdur")

# Input: 240135
# Output: 1
