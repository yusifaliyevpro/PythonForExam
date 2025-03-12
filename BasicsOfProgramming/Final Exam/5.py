N = 3

a = "12*3*4567*89"
x = [1, 2, 3, 4, 5, 6]
x.insert(a.rfind("*"), 100)
print(sum(x[::2]))
