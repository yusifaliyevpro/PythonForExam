# 28. Create a class Car with a method start_engine that takes 
# a boolean parameter N (True to start, False to stop the engine).

class Car:
    def __init__(self, model):
        self.model = model
    
    def start_engine(self, start):
        if start:
            print(f"{self.model} engine started.")
        else:
            print(f"{self.model} engine stopped.")

N = int(input("Enter 1 to start engine, 0 to stop engine: "))
start_engine = bool(N)
model = input("Enter car model: ")
car = Car(model)
car.start_engine(start_engine)