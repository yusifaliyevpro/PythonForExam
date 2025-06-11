# 22. Write a Python program that uses inheritance and polymorphism by creating two classes Employee and Manager, both having a get_salary() method. The Manager should return a higher salary than Employee.


class Employee:
    def get_salary(self):
        return 50000


class Manager(Employee):
    def get_salary(self):
        return 70000


employee = Employee()
manager = Manager()

print(f"Employee salary: {employee.get_salary()}")
print(f"Manager salary: {manager.get_salary()}")
