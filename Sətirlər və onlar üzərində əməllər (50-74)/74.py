a = input("Cümlə daxil edin: ").split(" ")
n = []

for i in a:
    n.append(i.count("a"))
print(n)

# Input: Azərbaycan Respublikası
# Output: [2, 1]
