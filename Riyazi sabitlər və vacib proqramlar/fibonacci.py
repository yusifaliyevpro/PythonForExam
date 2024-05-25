# n-ci fibonacci ədədinə qədər (n daxil) olan ədədlərin cəmini hesablayan proqram
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Ədəd daxil edin: "))
s = 0

for i in range(1, n+1):
    s += fibonacci(i)

print(s)

# Input: 5
# Output: 12
