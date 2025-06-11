# 21. Write a Python program that uses encapsulation to store and retrieve the balance in a bank account, ensuring that balance can't be directly modified from outside the class.

class BankAccount:
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
print("Current balance:", account.get_balance())
