# 19. Create a class Person with an __init__ method that takes name and age. Then, create a method greet() that prints a greeting message.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

person = Person("Alice", 30)
print(person.greet())
