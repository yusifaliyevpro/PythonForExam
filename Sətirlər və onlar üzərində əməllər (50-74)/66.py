a = input("Cümlə daxil edin: ")
s = ""

for i in a:
    if i == "a":
        s += "b"
    elif i == "b":
        s += "a"
    else:
        s += i
print(s)

# Input: how are you my brother
# Output: how bre you my arother
