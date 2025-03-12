N = 60

M = 20
while N != 0 and M != 0:
    if N > M:
        N = N % M
    else:
        M = M % N
print(N + M)
