# 29. Create an abstract base class Shape with an abstract method area(). Implement it in a derived class Circle.

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

N = float(input("Enter radius for circle (N): "))
circle = Circle(N)
print(f"Area of the circle: {circle.area()}")