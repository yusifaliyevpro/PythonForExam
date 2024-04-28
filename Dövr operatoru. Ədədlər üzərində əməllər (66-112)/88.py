s = 0


def c(x):
    m = 0
    for i in str(x):
        m += int(i)
    return m


for i in range(100, 1000):
    if i % 2 == 0 and i % 5 == 0 and c(i) >= 12:
        s += 1
print(s)

# Output: 28
