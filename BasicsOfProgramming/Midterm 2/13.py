# 13. Write a Python class Book that has methods to set and get the title and author.

class Book:
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
print(my_book.get_title(), "by", my_book.get_author())
