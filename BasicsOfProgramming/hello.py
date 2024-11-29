from string import printable
from time import sleep

hello = "Hello, World!"
s = ""

for i in hello:
    for j in printable:
        if i == j:
            s += j
            print(s)
            break
        else:
            print(s + j)
        sleep(0.006)
