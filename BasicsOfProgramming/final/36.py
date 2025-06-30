# 36. Define a class to convert temperature from Celsius to Fahrenheit.

class TemperatureConverter:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

N = float(input("Enter temperature in Celsius: "))
tc = TemperatureConverter(N)
print("Temperature in Fahrenheit:", tc.to_fahrenheit())