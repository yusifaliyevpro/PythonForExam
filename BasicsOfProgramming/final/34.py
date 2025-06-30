# 34. Define a class that calculates factorial of N.

class Factorial:
    def __init__(self, N):
        self.N = N
    
    def compute(self):
        result = 1
        for i in range(2, self.N + 1):
            result *= i
        return result

N = int(input("Enter a number to calculate its factorial: "))
f = Factorial(N)
print(f"Factorial of {N}: {f.compute()}")