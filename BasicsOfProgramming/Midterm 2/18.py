# 18. Write a Python function that uses polymorphism by accepting different objects (e.g., Computer, Phone) that have a start() method and calls that method on the passed object.


class Computer:
    def start(self):
        return "Booting up the computer..."


class Phone:
    def start(self):
        return "Turning on the phone..."


def start_device(device):
    print(device.start())


computer = Computer()
phone = Phone()

start_device(computer)
start_device(phone)
