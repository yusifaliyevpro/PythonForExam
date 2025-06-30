# 30. Create a class BankAccount with private attributes for balance. Add methods to deposit and withdraw money.

class BankAccount:
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
print(f"Remaining balance: {account.get_balance()}")