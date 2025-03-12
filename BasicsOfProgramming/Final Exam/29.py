N = 15

S = 0
for k in range(1, N):
    if k % 3 != 0:
        continue
    S += k
print(S)
