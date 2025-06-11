# 16. Write a Python program using inheritance where the base class Shape has an area method, and a derived class Circle overrides this method to calculate the area of a circle.

import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

circle = Circle(5)
print(f"Area of the circle: {circle.area()}")
