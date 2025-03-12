# 14. Longest Common Prefix

a = input("Enter the list (with space): ").split()
s = ""

for i in range(len(min(a, key=len))):
    t = a[0][i]
    if all(map(lambda x: x[i] == t, a)):
        s += t

print(s)
