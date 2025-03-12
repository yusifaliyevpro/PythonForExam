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
        sleep(0.006)
