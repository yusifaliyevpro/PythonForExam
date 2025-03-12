# 1. Two Sum

a = input("Enter the list (with space): ")
a = list(map(int, a.split()))
target = int(input("Enter number: "))
b = []
for i in range(len(a) - 1):
    if (a[i] + a[i + 1]) == target:
        b.append(i)
        b.append(i + 1)
print(b)
