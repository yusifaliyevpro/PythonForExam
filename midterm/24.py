# 24. Two Sum

a = input("Enter the list (with space): ")
a = list(map(int, a.split()))

target = int(input("Enter a Number: "))

for i in range(len(a)):
    if i != len(a) - 1 and a[i] + a[i + 1] == target:
        print(i, i + 1)
