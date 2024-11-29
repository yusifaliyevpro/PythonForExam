# 23. Roman to Integer

n = input("Enter roman Number: ")
s = 0
dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

for i in range(len(n)):
    if i != 0 and dict[n[i]] > dict[n[i - 1]]:
        s += dict[n[i]] - 2 * dict[n[i - 1]]
    else:
        s += dict[n[i]]
print(s)
