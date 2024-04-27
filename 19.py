a = input("2-dən böyük ədəd daxil edin: ")
b = []

for i in a:
    b.append(i)

b.sort()
b.reverse()
print(int("".join(b)))
