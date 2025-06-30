# 40. Class to Reverse a Number:

class ReverseNumber:
    def __init__(self, N):
        self.N = N
    
    def reverse(self):
        return int(str(self.N)[::-1])

N = int(input("Enter a number (N): "))
obj = ReverseNumber(N)
print(f"Reversed number: {obj.reverse()}")