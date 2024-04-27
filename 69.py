n = int(input())
s = 0

for i in range(1, n+1, 2):
    s += (1/i)**i
print(s)

# Input:
# 100
# Output:
# 1.037358253887399

# Input:
# 10000
# Output:
# 1.037358253887399

# Input:
# 32948394
# Output:
# 1.037358253887399
