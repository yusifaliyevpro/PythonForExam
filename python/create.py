import os

path = "Ev tapşırıqları/03.05.2024"

for i in range(93, 101):
    a = open(os.path.join(path, f"{i}.py"), 'w')
    a.write("# Write a program")
    a.close()

# for i in range(1, 26):
#     os.remove(os.path.join(path, f"{i}.py"))
