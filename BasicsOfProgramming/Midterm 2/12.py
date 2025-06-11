# 12. Create a Python class Vehicle and a derived class Car that inherits from Vehicle. Include a method in Car to display the sound it makes.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def sound(self):
        return "Some generic vehicle sound"

class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)

    def sound(self):
        return "Vroom"

my_car = Car("Toyota")
print(f"The {my_car.brand} goes: {my_car.sound()}")
