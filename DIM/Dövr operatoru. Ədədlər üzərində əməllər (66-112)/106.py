a = input("Sətiri daxil edin: ")
b = []

for i in a:
    if b.count(i) == 0:
        b.append(i)

print(b)

# Input: riyaziyyat
# Output: ['r', 'i', 'y', 'a', 'z', 't']
