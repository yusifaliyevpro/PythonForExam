from datetime import datetime
a = []
b = []

for i in range(0, 6):
    if len(a) != 3:
        a.append(int(input()))
    else:
        b.append(int(input()))
saat1, deq1, san1 = a
saat2, deq2, san2 = b
a = datetime(saat1, deq1, san1)
b = datetime(saat2, deq2, san2)
a -= b

print(a.total_seconds())
