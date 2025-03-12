# 83. Remove Duplicates from Sorted List


a = input("Enter the list (with space): ")
a = list(map(int, a.split()))

for i in a:
    if a.count(i) != 1:
        a.remove(i)
print(a)
