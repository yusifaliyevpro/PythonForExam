class Bike:
    __slots__ = ["wheels", "type"]

p1 = Bike()

p1.wheels = 4
p1.type = "mountain"

print(p1.wheels, p1.type)