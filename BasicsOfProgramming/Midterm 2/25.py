# 25. Write a program that creates a Shape class with a method get_area(). Then create Rectangle and Circle classes that inherit from Shape and implement get_area() accordingly.

import math

class Shape:
    def get_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

rectangle = Rectangle(10, 5)
circle = Circle(7)

print(f"Rectangle area: {rectangle.get_area()}")
print(f"Circle area: {circle.get_area()}")
