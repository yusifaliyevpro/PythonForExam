import os

path = ""

for i in range(84, 104):
    a = open(os.path.join(path, f"{i}.py"), 'x')
    a.close()

# for i in range(1, 26):
#     os.remove(os.path.join(path, f"{i}.py"))
