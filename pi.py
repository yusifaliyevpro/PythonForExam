# GREGORY/LEIBNIZ Düsturu
n = int(input())+1
s = 0

for i in range(0, n):
    s += ((-1)**i)/(2*i+1)
print(4*s)
