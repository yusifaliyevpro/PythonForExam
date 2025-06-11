# 28. Write a Python program that demonstrates method overriding by creating a class Vehicle with a start() method, and a subclass Car that overrides this method.

class Vehicle:
    def start(self):
        return "Starting the vehicle..."

class Car(Vehicle):
    def start(self):
        return "Starting the car engine..."

vehicle = Vehicle()
car = Car()

print(vehicle.start())
print(car.start())
