N = 18

K = (150, 250)[N % 5 != 0]
K = (K // 15) % 5
M = K - 1
"""
if M<=3:
    K+=1
else:
    K+=2
"""
print(K)
