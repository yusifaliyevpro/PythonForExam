# 16. Random Password Generator
from string import printable
from random import choice

printable = printable.strip()
n = int(input("Length of Password: "))
s = ""
for i in range(n):
    s += choice(printable)
print(s)
