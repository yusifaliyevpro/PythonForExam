# 30. Write a Python program that uses polymorphism to call a display() method on different types of objects (e.g., Book, Magazine) which each implement display() differently.

class Book:
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
show_content(magazine)
