import os

path = "test"

tasks = [
    "",
    "Gülnarə Müəllimə.",
    "Elmin",
    "Günel",
    "Yusif",
    "Əli",
]


for i in range(1, len(tasks)):
    a = open(os.path.join(path, f"{i}.py"), 'w', encoding="utf-8")
    a.write(f"# {i}. {tasks[i]}")
    a.close()

# for i in range(1, 26):
#     os.remove(os.path.join(path, f"{i}.py"))
