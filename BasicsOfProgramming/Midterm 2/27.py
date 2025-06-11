# 27. Write a Python program that implements an abstract class Shape and create a derived class Square that implements the area() method.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

square = Square(4)
print(f"Area of the square: {square.area()}")
