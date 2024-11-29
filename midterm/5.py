# 5. List of Multiples

n = int(input("Enter a Number: "))
limit = int(input("Enter the Limit: "))
a = []
for i in range(1, limit + 1):
    a.append(n * i)

print(a)
