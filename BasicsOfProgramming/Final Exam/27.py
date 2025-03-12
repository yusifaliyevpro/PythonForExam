N = 3

H = [
    "baku",
    "Moskva",
    "Antaliya",
    "Berlin",
    "minsk",
    "Kiev",
    "tbilisi",
    "ankara",
    "Paris",
]
B = [k.upper() for k in H]
F = B.pop(N)
print(F)
