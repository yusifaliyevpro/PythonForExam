# 38. Class with N and Sum Method:

class SumClass:
    def __init__(self, N):
        self.N = N
    
    def sum_numbers(self):
        return sum(range(1, self.N + 1))

N = int(input("Enter a number (N): "))
obj = SumClass(N)
result = obj.sum_numbers()
print(f"The sum of numbers from 1 to {N} is: {result}")