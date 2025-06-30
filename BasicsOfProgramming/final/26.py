# 26. Create a class called Rectangle that calculates the area of a rectangle. 
# Use the values of N (length and width) to compute the area.

class Rectangle:
    def __init__(self, N):
        self.length = N
        self.width = N
    
    def area(self):
        return self.length * self.width

N = float(input("Enter a value for N (length and width of rectangle): "))
rect = Rectangle(N)
print(f"Area of rectangle: {rect.area()}")