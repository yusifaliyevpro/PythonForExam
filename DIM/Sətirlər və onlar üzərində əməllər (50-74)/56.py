a = input()
s = 0

for i in a:
    if a.count(i) == 1:
        s += 1
print(s)

# Input: Hello World
# Output: 6

# Input: ananas
# Output: 1
