# 19. Degree of symmetry

n = int(input())
s = 0
A = []

while n != 0:
    A.append(n % 10)
    n //= 10

if len(A) % 2 == 1:
    s += 1

for i in range(len(A) // 2):
    if A[i] == A[len(A) - i - 1]:
        s += 1

print(s)
