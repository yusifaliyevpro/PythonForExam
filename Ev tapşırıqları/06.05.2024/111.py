n = int(input('Ədəd daxil edin: '))
a = []


def fib(n):
    if n in {1, 0}:
        return n
    return fib(n-1) + fib(n-2)


for i in range(0, n):
    a.append(fib(i))
print(a)

# Input: 10
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
