# 26. Create a class Student with a __str__ method to return a string representation of a student's details (name, age, grade).

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"Student {self.name}, Age: {self.age}, Grade: {self.grade}"

student = Student("Alice", 20, "A")
print(student)
