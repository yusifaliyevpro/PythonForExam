N = 6

# a = input()
a = "0123456789A"
k = a[N::2] + a[N::-2]
k = 2 * k
print(k)
