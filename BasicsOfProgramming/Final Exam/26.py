N = 4

H = [
    "alma",
    "nar",
    "encir",
    "chiyelek",
    "qaragat",
    "shaftali",
    "erik",
    "armud",
    "gavali",
]
B = sorted(H, key=len)
F = B.pop(N)
print(F)
