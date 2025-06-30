# 39. Class to Check if N is Even or Odd:

class CheckEvenOdd:
    def __init__(self, N):
        self.N = N
    
    def is_even(self):
        return self.N % 2 == 0

N = int(input("Enter a number (N): "))
obj = CheckEvenOdd(N)
if obj.is_even():
    print(f"{N} is even.")
else:
    print(f"{N} is odd.")