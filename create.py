import os

path = "Dövr operatoru. Ədədlər üzərində əməllər (66-112)"

for i in range(102, 113):
    a = open(os.path.join(path, f"{i}.py"), 'w')
    a.write("# Write a program")
    a.close()

# for i in range(1, 26):
#     os.remove(os.path.join(path, f"{i}.py"))
