class Car:
    wheels = 4  # Class/static variable
    def __init__(self):
        self.brand = "BMW" # Instance Variable
        self.mil = 10

c1 = Car()
c2 = Car()
Car.wheels = 5
c1.mil = 6
print(f"Car name: {c1.brand}, milleage: {c1.mil}, wheels: {c1.wheels}")
print(f"Car name: {c2.brand}, milleage: {c2.mil}, wheels: {c2.wheels}")