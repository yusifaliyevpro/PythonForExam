n = int(input("2-dən böyük ədəd daxil edin: "))-1
a = True
while a:
    if n % 2 == 0:
        print(n)
        a = False
    else:
        n -= 1

# Input: 6
# Output: 4

# Input: 9
# Output: 8
