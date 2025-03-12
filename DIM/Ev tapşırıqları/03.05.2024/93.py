# Fibonaççi sırasının n-ci həddini tapan proqram yazın 1, 1, 2, 3, 5, 8, 13...

def fibonacci(n):
    if n in {0, 1}:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)


n = int(input("Həddin nömrəsini daxil edin: "))
print(fibonacci(n))

# Input: 5
# Output: 5

# Input: 6
# Output: 8
