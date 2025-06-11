# 29. Create a Python class Library that keeps a list of books. Write a method add_book() to add books to the library.

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

library = Library()
library.add_book("1984")
library.add_book("Brave New World")
print(f"Books in the library: {library.books}")
