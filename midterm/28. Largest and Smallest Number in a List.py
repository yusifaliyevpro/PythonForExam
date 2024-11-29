# 28. Largest and Smallest Number in a List

a = input("Enter the list (with space): ")
a = list(map(int, a.split()))

print(f"Max: {max(a)}, Min: {min(a)}")
