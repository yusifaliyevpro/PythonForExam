# 37. Class to Multiply a Number N by Another Value:

class MultiplyByN:
    def __init__(self, N):
        self.N = N
    
    def multiply(self, x):
        return x * self.N

N = float(input("Enter a number (N): "))
obj = MultiplyByN(N)
result = obj.multiply(3)
print(f"{N} multiplied by 3 is: {result}")