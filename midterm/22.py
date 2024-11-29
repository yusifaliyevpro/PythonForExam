# 22. Finding Duplicates

a = input("Enter the list (with space): ")
a = list(map(int, a.split()))
b = []
for i in a:
    if a.count(i) != 1 and b.count(i) == 0:
        print(i)
        b.append(i)
