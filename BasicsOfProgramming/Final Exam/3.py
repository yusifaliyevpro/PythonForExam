N = 22

if N < 20:
    M = str(N)
else:
    M = "x" + str(N)
var = "a" + ("x" if M.isdigit() else "y") + "b"
print(var)
