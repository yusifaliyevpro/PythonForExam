n = input("Ədədi daxil edin: ")
s = 0
m = 0

for i in n:
    i = int(i)
    if i % 2 == 1:
        s += i
        m += 1
print(f"{s} {m}")

# Input: Ədədi daxil edin: 3756
# Output: 15 3
