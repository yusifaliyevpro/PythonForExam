# 66. Plus One

a = input("Enter the list (with space): ")
a = list(reversed(list(map(int, a.split()))))
a[0] += 1
for i in range(len(a)):
    if a[i] == 10:
        a[i] = 0
        a[i + 1] += 1

a = list(reversed(a))
print(a)
