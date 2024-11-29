# 30. Pascal's Triangle
n = int(input("Enter a number: "))
for row in range(1, n + 1):
    c = 1
    print((n - row) * " ", end="")

    for i in range(1, row + 1):
        print(c, end=" ")
        c = c * (row - i) // i
    print()
