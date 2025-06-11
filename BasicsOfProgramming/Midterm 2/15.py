# 15. Demonstrate the use of encapsulation in Python by creating a class Account with private attributes for balance and a method to deposit money.


class Account:
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
print(f"Account balance: {acc.get_balance()}")
