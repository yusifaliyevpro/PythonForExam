# 31. What is the __init__ method in a class? Provide an example.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

N = input("Enter a value for car details (N): ")
car1 = Car(N, N, N)
print(f"Car make: {car1.make}, Car model: {car1.model}, Car year: {car1.year}")