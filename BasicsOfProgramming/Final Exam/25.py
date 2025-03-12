N = 30

import math

m = N / 2
z = m // 5
k = z * math.modf(m)
# k=len(k)*z
print(k)

# Error verməsi normaldır, N-dən asılı deyil
