# 33. Write a class that checks if a number N is a prime number.

class PrimeChecker:
    def __init__(self, N):
        self.N = N
    
    def is_prime(self):
        if self.N < 2:
            return False
        for i in range(2, int(self.N ** 0.5) + 1):
            if self.N % i == 0:
                return False
        return True

N = int(input("Enter a number to check if it's prime: "))
checker = PrimeChecker(N)
print(f"Is {N} prime? {checker.is_prime()}")