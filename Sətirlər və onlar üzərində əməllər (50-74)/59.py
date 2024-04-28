a = input("2-dən böyük ədəd daxil edin: ")
b = []

for i in a:
    b.append(i)

b.sort()
b.reverse()
print(int("".join(b)))

# Input: 34213
# Output: 43321

# Input: 3081
# Output: 8310
