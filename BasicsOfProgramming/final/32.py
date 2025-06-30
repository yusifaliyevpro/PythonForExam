# 32. What is method overloading and does Python support it? Explain the concept of method 
# overloading and demonstrate how Python handles it.

class Printer:
    def print_message(self, message=None, repeat=1):
        if message:
            print((message + "\n") * repeat)

N = int(input("Enter how many times to print the message (N): "))
printer = Printer()
printer.print_message("Hello", N)