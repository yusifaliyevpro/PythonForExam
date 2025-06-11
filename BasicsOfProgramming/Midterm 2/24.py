# 24. Implement a Person class in Python where the age is stored as a private attribute, and provide getter and setter methods to access and modify the age.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def set_age(self, age):
        if age > 0:
            self.__age = age

    def get_age(self):
        return self.__age

person = Person("John", 25)
person.set_age(30)
print(f"{person.name}'s age: {person.get_age()}")
