a = input("Sətir daxil edin: ")
b = 0
c = 0

for i in a:
    if i == 's':
        b += 1
        if c < b:
            c = b
    else:
        b = 0
print(c)

# Input: asbbbsssbc
# Output: 3
