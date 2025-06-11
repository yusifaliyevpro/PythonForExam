import os

# Klasör adı
path = "midterm"
os.makedirs(path, exist_ok=True)

# 11'den başlayarak tüm 30 soru-cevap
qa_pairs = [
    (
        "Write a Python class that implements a basic Car object with attributes like make, model, and year, and a method to display the car's information.",
        """class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

my_car = Car("Toyota", "Corolla", 2021)
print(my_car.display_info())""",
    ),
    (
        "Create a Python class Vehicle and a derived class Car that inherits from Vehicle. Include a method in Car to display the sound it makes.",
        """class Vehicle:
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
print(f"The {my_car.brand} goes: {my_car.sound()}")""",
    ),
    (
        "Write a Python class Book that has methods to set and get the title and author.",
        """class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

my_book = Book("1984", "George Orwell")
print(my_book.get_title(), "by", my_book.get_author())""",
    ),
    (
        "Implement a Python class Rectangle with attributes for width and height, and a method area() that calculates the area of the rectangle.",
        """class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(4, 5)
print(f"Area of the rectangle: {rect.area()}")""",
    ),
    (
        "Demonstrate the use of encapsulation in Python by creating a class Account with private attributes for balance and a method to deposit money.",
        """class Account:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}, new balance: {self.__balance}")
        else:
            print("Deposit amount must be positive")

    def get_balance(self):
        return self.__balance

acc = Account(100)
acc.deposit(50)
print(f"Account balance: {acc.get_balance()}")""",
    ),
    (
        "Write a Python program using inheritance where the base class Shape has an area method, and a derived class Circle overrides this method to calculate the area of a circle.",
        """import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

circle = Circle(5)
print(f"Area of the circle: {circle.area()}")""",
    ),
    (
        "Create a Python class Student with a constructor that takes the student's name, age, and grade. Include a method display_info() to show the student's details.",
        """class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

student = Student("John", 16, "A")
print(student.display_info())""",
    ),
    (
        "Write a Python function that uses polymorphism by accepting different objects (e.g., Computer, Phone) that have a start() method and calls that method on the passed object.",
        """class Computer:
    def start(self):
        return "Booting up the computer..."

class Phone:
    def start(self):
        return "Turning on the phone..."

def start_device(device):
    print(device.start())

computer = Computer()
phone = Phone()

start_device(computer)
start_device(phone)""",
    ),
    (
        "Create a class Person with an __init__ method that takes name and age. Then, create a method greet() that prints a greeting message.",
        """class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

person = Person("Alice", 30)
print(person.greet())""",
    ),
    (
        "Demonstrate the principle of abstraction by creating an abstract base class Vehicle with an abstract method move(), and create a derived class Car that implements this method.",
        """from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "The car is driving"

car = Car()
print(car.move())""",
    ),
    (
        "Write a Python program that uses encapsulation to store and retrieve the balance in a bank account, ensuring that balance can't be directly modified from outside the class.",
        """class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
print("Current balance:", account.get_balance())""",
    ),
    (
        "Write a Python program that uses inheritance and polymorphism by creating two classes Employee and Manager, both having a get_salary() method. The Manager should return a higher salary than Employee.",
        """class Employee:
    def get_salary(self):
        return 50000

class Manager(Employee):
    def get_salary(self):
        return 70000

employee = Employee()
manager = Manager()

print(f"Employee salary: {employee.get_salary()}")
print(f"Manager salary: {manager.get_salary()}")""",
    ),
    (
        "Create a Python class Counter that tracks the number of times an object is created, using a class-level variable to store the count.",
        """class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
print(f"Total objects created: {Counter.count}")""",
    ),
    (
        "Implement a Person class in Python where the age is stored as a private attribute, and provide getter and setter methods to access and modify the age.",
        """class Person:
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
print(f"{person.name}'s age: {person.get_age()}")""",
    ),
    (
        "Write a program that creates a Shape class with a method get_area(). Then create Rectangle and Circle classes that inherit from Shape and implement get_area() accordingly.",
        """import math

class Shape:
    def get_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

rectangle = Rectangle(10, 5)
circle = Circle(7)

print(f"Rectangle area: {rectangle.get_area()}")
print(f"Circle area: {circle.get_area()}")""",
    ),
    (
        "Create a class Student with a __str__ method to return a string representation of a student's details (name, age, grade).",
        """class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"Student {self.name}, Age: {self.age}, Grade: {self.grade}"

student = Student("Alice", 20, "A")
print(student)""",
    ),
    (
        "Write a Python program that implements an abstract class Shape and create a derived class Square that implements the area() method.",
        """from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

square = Square(4)
print(f"Area of the square: {square.area()}")""",
    ),
    (
        "Write a Python program that demonstrates method overriding by creating a class Vehicle with a start() method, and a subclass Car that overrides this method.",
        """class Vehicle:
    def start(self):
        return "Starting the vehicle..."

class Car(Vehicle):
    def start(self):
        return "Starting the car engine..."

vehicle = Vehicle()
car = Car()

print(vehicle.start())
print(car.start())""",
    ),
    (
        "Create a Python class Library that keeps a list of books. Write a method add_book() to add books to the library.",
        """class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

library = Library()
library.add_book("1984")
library.add_book("Brave New World")
print(f"Books in the library: {library.books}")""",
    ),
    (
        "Write a Python program that uses polymorphism to call a display() method on different types of objects (e.g., Book, Magazine) which each implement display() differently.",
        """class Book:
    def display(self):
        return "Displaying book content"

class Magazine:
    def display(self):
        return "Displaying magazine content"

def show_content(item):
    print(item.display())

book = Book()
magazine = Magazine()

show_content(book)
show_content(magazine)""",
    ),
]

# Dosya yazma
start_index = 11
for idx, (question, code) in enumerate(qa_pairs, start=start_index):
    filename = os.path.join(path, f"{idx}.py")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {idx}. {question}\n\n{code}\n")

print(f"{len(qa_pairs)} dosya başarıyla '{path}' klasörüne yazıldı.")
