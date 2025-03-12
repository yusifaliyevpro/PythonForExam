# 1-dən (n-1)-ə kimi olan ədədlərin cəmini tapan proqram yazın

n = int(input("Ədəd daxil edin: "))
s = 0

for i in range(1, n):
    s += i
print(s)

# Input: 101
# Output: 5050
