# 35. Write a class that returns a multiplication table of a number N up to 10.

class MultiplicationTable:
    def __init__(self, N):
        self.N = N
    
    def print_table(self):
        for i in range(1, 11):
            print(f"{self.N} x {i} = {self.N * i}")

N = int(input("Enter a number to print its multiplication table: "))
table = MultiplicationTable(N)
table.print_table()