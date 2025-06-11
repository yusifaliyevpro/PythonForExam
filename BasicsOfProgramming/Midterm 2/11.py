# 11. Write a Python class that implements a basic Car object with attributes like make, model, and year, and a method to display the car's information.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

my_car = Car("Toyota", "Corolla", 2021)
print(my_car.display_info())
