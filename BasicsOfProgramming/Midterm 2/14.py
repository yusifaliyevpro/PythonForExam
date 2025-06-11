# 14. Implement a Python class Rectangle with attributes for width and height, and a method area() that calculates the area of the rectangle.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(4, 5)
print(f"Area of the rectangle: {rect.area()}")
