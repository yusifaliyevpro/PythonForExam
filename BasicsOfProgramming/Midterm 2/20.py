# 20. Demonstrate the principle of abstraction by creating an abstract base class Vehicle with an abstract method move(), and create a derived class Car that implements this method.

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        return "The car is driving"


car = Car()
print(car.move())
