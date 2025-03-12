# 87. Robot


def main():
    a = 0
    n = 0
    p = 0
    c = input()

    for i in c:
        if i == "R":
            a += 1
        if i == "L":
            a -= 1
        if p < a:
            p = a
        if n > a:
            n = a

    if n == 0:
        print(p + 1)
    elif p == 0:
        print(abs(n) + 1)
    else:
        print(abs(n) + p + 1)


main()
