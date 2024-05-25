import os

path = "Ev tapşırıqları/29.05.2024"

for i in range(117, 138):
    a = open(os.path.join(path, f"{i}.py"), 'x')
    a.close()

# for i in range(1, 26):
#     os.remove(os.path.join(path, f"{i}.py"))
