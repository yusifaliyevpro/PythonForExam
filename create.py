import os

# Klasör adı
path = "final"
os.makedirs(path, exist_ok=True)

qa_pairs = [
    (
        "The number N is given. A number is selected from the spinner. When the OK button is clicked, if the number in the spinner is greater than N, the warning window displays 'Yes', otherwise 'No'. Write the program code for this scenario.",
        # Bu soru PyQt5 ile ilgili olduğu için kod yok
        "",
    ),
    (
        "N is given. The value of the quantity is entered from LineEdit. When the OK button is clicked, we will be notified if the entered number is equal to N.",
        # Bu soru PyQt5 ile ilgili olduğu için kod yok
        "",
    ),
    (
        "The number N is given. The price of the item is entered from TextEdit. When the OK button is clicked, if the entered number is equal to N, the warning window displays 'Yes', otherwise 'No'. Write the program code for this scenario.",
        # Bu soru PyQt5 ile ilgili olduğu için kod yok
        "",
    ),
    (
        "The number N is given. The value of the number is entered from LineEdit. When the OK button is clicked, the number entered from LineEdit is added to the value of N and written to TextEdit. Write the program code for this scenario.",
        # Bu soru PyQt5 ile ilgili olduğu için kod yok
        "",
    ),
    (
        "The number N is given. The value of the number is entered from TextEdit. When the OK button is clicked, the number entered from TextEdit is multiplied by the value of N and written to LineEdit. Write the program code for this scenario.",
        # Bu soru PyQt5 ile ilgili olduğu için kod yok
        "",
    ),
    (
        "Create a class called Rectangle that calculates the area of a rectangle. Use the values of N (length and width) to compute the area.",
        """class Rectangle:
    def __init__(self, N):
        self.length = N
        self.width = N
    
    def area(self):
        return self.length * self.width

N = float(input("Enter a value for N (length and width of rectangle): "))
rect = Rectangle(N)
print(f"Area of rectangle: {rect.area()}")""",
    ),
    (
        "Create a derived class Square from the Rectangle class, where the length and width are the same. Compute the area.",
        """class Rectangle:
    def __init__(self, N):
        self.length = N
        self.width = N
    
    def area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length)

N = float(input("Enter side length for square (N): "))
square = Square(N)
print(f"Area of square: {square.area()}")""",
    ),
    (
        "Create a class Car with a method start_engine that takes a boolean parameter N (True to start, False to stop the engine).",
        """class Car:
    def __init__(self, model):
        self.model = model
    
    def start_engine(self, start):
        if start:
            print(f"{self.model} engine started.")
        else:
            print(f"{self.model} engine stopped.")

N = int(input("Enter 1 to start engine, 0 to stop engine: "))
start_engine = bool(N)
model = input("Enter car model: ")
car = Car(model)
car.start_engine(start_engine)""",
    ),
    (
        "Create an abstract base class Shape with an abstract method area(). Implement it in a derived class Circle.",
        """from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

N = float(input("Enter radius for circle (N): "))
circle = Circle(N)
print(f"Area of the circle: {circle.area()}")""",
    ),
    (
        "Create a class BankAccount with private attributes for balance. Add methods to deposit and withdraw money.",
        """class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance.")
    
    def get_balance(self):
        return self.__balance

N = float(input("Enter the amount (N): "))
account = BankAccount(N)
account.deposit(N)
account.withdraw(N)
print(f"Remaining balance: {account.get_balance()}")""",
    ),
    (
        "What is the __init__ method in a class? Provide an example.",
        """class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

N = input("Enter a value for car details (N): ")
car1 = Car(N, N, N)
print(f"Car make: {car1.make}, Car model: {car1.model}, Car year: {car1.year}")""",
    ),
    (
        "What is method overloading and does Python support it? Explain the concept of method overloading and demonstrate how Python handles it.",
        """class Printer:
    def print_message(self, message=None, repeat=1):
        if message:
            print((message + "\\n") * repeat)

N = int(input("Enter how many times to print the message (N): "))
printer = Printer()
printer.print_message("Hello", N)""",
    ),
    (
        "Write a class that checks if a number N is a prime number.",
        """class PrimeChecker:
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
print(f"Is {N} prime? {checker.is_prime()}")""",
    ),
    (
        "Define a class that calculates factorial of N.",
        """class Factorial:
    def __init__(self, N):
        self.N = N
    
    def compute(self):
        result = 1
        for i in range(2, self.N + 1):
            result *= i
        return result

N = int(input("Enter a number to calculate its factorial: "))
f = Factorial(N)
print(f"Factorial of {N}: {f.compute()}")""",
    ),
    (
        "Write a class that returns a multiplication table of a number N up to 10.",
        """class MultiplicationTable:
    def __init__(self, N):
        self.N = N
    
    def print_table(self):
        for i in range(1, 11):
            print(f"{self.N} x {i} = {self.N * i}")

N = int(input("Enter a number to print its multiplication table: "))
table = MultiplicationTable(N)
table.print_table()""",
    ),
    (
        "Define a class to convert temperature from Celsius to Fahrenheit.",
        """class TemperatureConverter:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

N = float(input("Enter temperature in Celsius: "))
tc = TemperatureConverter(N)
print("Temperature in Fahrenheit:", tc.to_fahrenheit())""",
    ),
    (
        "Class to Multiply a Number N by Another Value:",
        """class MultiplyByN:
    def __init__(self, N):
        self.N = N
    
    def multiply(self, x):
        return x * self.N

N = float(input("Enter a number (N): "))
obj = MultiplyByN(N)
result = obj.multiply(3)
print(f"{N} multiplied by 3 is: {result}")""",
    ),
    (
        "Class with N and Sum Method:",
        """class SumClass:
    def __init__(self, N):
        self.N = N
    
    def sum_numbers(self):
        return sum(range(1, self.N + 1))

N = int(input("Enter a number (N): "))
obj = SumClass(N)
result = obj.sum_numbers()
print(f"The sum of numbers from 1 to {N} is: {result}")""",
    ),
    (
        "Class to Check if N is Even or Odd:",
        """class CheckEvenOdd:
    def __init__(self, N):
        self.N = N
    
    def is_even(self):
        return self.N % 2 == 0

N = int(input("Enter a number (N): "))
obj = CheckEvenOdd(N)
if obj.is_even():
    print(f"{N} is even.")
else:
    print(f"{N} is odd.")""",
    ),
    (
        "Class to Reverse a Number:",
        """class ReverseNumber:
    def __init__(self, N):
        self.N = N
    
    def reverse(self):
        return int(str(self.N)[::-1])

N = int(input("Enter a number (N): "))
obj = ReverseNumber(N)
print(f"Reversed number: {obj.reverse()}")""",
    ),
    (
        "Find the N Employees Who Have Been with the Company the Longest. Retrieve the first N employees who have been with the company the longest, based on HireDate.",
        """SET @N = The given value; -- Set the number of employees to retrieve (you can change this value as needed)
SELECT EmployeeID, EmployeeName, HireDate
FROM Employees
ORDER BY HireDate ASC
LIMIT @N;""",
    ),
    (
        "List N Products That Are Out of Stock. Retrieve the N products that are out of stock from the Products table.",
        """SET @N = The given value; -- Set the number of products to retrieve (you can change this value as needed)
SELECT ProductID, ProductName, StockQuantity
FROM Products
WHERE StockQuantity = 0
LIMIT @N;""",
    ),
    (
        "Calculate the Total Price of the First N Products. Calculate the total price of the first N products from the Products table.",
        """SET @N = The given value;
SELECT SUM(Price) AS TotalPrice
FROM (
    SELECT Price
    FROM Products
    LIMIT @N
) AS TopNProducts;""",
    ),
    (
        "Get the N Highest Salaries. Retrieve the N employees with the highest salaries from the Employees table.",
        """SET @N = The given value;
SELECT EmployeeID, EmployeeName, Salary
FROM Employees
ORDER BY Salary DESC
LIMIT @N;""",
    ),
    (
        "Get the N Smallest Prices. Get the N smallest prices from the Products table.",
        """SET @N = The given value;
-- Retrieve the N products with the smallest prices
SELECT ProductID, ProductName, Price
FROM Products
ORDER BY Price ASC
LIMIT @N;""",
    ),
    (
        "List N Employees with the Most Hours Worked. Retrieve the N employees with the most hours worked from the EmployeeHours table.",
        """SET @N = The given value;
SELECT EmployeeID, SUM(HoursWorked) AS TotalHours
FROM EmployeeHours
GROUP BY EmployeeID
ORDER BY TotalHours DESC
LIMIT @N;""",
    ),
    (
        "Find the N Oldest Employees. You have to get the first N employees with the oldest hire dates from the Employees table.",
        """SET @N = The given value;
SELECT EmployeeID, EmployeeName, HireDate
FROM Employees
ORDER BY HireDate ASC
LIMIT @N;""",
    ),
    (
        "Calculate the Average of the First N Salaries. You have to calculate the average salary of the first N employees from the Employees table.",
        """SET @N = The given value;
SELECT AVG(Salary) AS AvgSalary
FROM (
    SELECT Salary
    FROM Employees
    ORDER BY EmployeeID
    LIMIT @N
) AS FirstNSalaries;""",
    ),
    (
        "Find the N Customers Who Have Spent the Most. You have to find the top N customers who have spent the most on products. Assume there is a Sales table with CustomerID and Amount.",
        """SET @N = The given value;
SELECT CustomerID, SUM(Amount) AS TotalSpent
FROM Sales
GROUP BY CustomerID
ORDER BY TotalSpent DESC
LIMIT @N;""",
    ),
    (
        "Delete the N Oldest Products. You need to delete the first N products that were added the earliest in the Products table, based on their ProductID.",
        """SET @N = The given value;
DELETE FROM Products
WHERE ProductID IN (
    SELECT ProductID
    FROM Products
    ORDER BY ProductID ASC
    LIMIT @N
);""",
    ),
]

# Dosya yazma
start_index = 21
for idx, (question, code) in enumerate(qa_pairs, start=start_index):
    filename = os.path.join(path, f"{idx}.py")
    with open(filename, "w", encoding="utf-8") as f:
        if code.strip():  # Eğer kod varsa
            f.write(f"# {idx}. {question}\n\n{code}\n")
        else:  # Kod yoksa sadece soruyu yaz
            f.write(f"# {idx}. {question}\n\n")

print(f"{len(qa_pairs)} dosya başarıyla '{path}' klasörüne yazıldı.")
