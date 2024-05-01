a = list(input("8-lik say sistemində ədəd daxil edin: "))
a.reverse()
m = 0
s = 0
for i in a:
    i = int(i)
    s += i*8**m
    m += 1
print(s)

# Input: 72
# Output: 58
