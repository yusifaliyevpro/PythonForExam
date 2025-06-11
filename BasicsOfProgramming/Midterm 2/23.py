# 23. Create a Python class Counter that tracks the number of times an object is created, using a class-level variable to store the count.

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
print(f"Total objects created: {Counter.count}")
