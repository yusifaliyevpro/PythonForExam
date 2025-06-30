# 27. Create a derived class Square from the Rectangle class, where the length and width are the same. Compute the area.

class Rectangle:
    def __init__(self, N):
        self.length = N
        self.width = N
    
    def area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length)

N = float(input("Enter side length for square (N): "))
square = Square(N)
print(f"Area of square: {square.area()}")