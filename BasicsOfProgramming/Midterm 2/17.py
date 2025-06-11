# 17. Create a Python class Student with a constructor that takes the student's name, age, and grade. Include a method display_info() to show the student's details.

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

student = Student("John", 16, "A")
print(student.display_info())
