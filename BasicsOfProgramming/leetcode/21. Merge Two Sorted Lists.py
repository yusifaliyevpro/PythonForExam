# 21. Merge Two Sorted Lists

l1 = input("Enter the list (with space): ")
l1 = list(map(int, l1.split()))
l2 = input("Enter the list (with space): ")
l2 = list(map(int, l2.split()))

print(sorted(l1 + l2))
