def check(a):
    m = 0
    for i in str(a):
        if int(i) % 2 == 0:
            m += 1
    if m == 3:
        return True
    else:
        return False


s = 0
for i in range(100, 1000):
    if check(i):
        s += i
print(s)  # Output: 54400
