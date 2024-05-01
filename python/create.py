import os

path = "Ev tapşırıqları/01.05.2024"

for i in range(85, 93):
    a = open(os.path.join(path, f"{i}.py"), 'w')
    a.write("# Write a program")
    a.close()

# for i in range(1, 26):
#     os.remove(os.path.join(path, f"{i}.py"))
