class student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()  # () is creating a instance in it

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class laptop:

        def __init__(self):
            self.brand = 'Asus'
            self.cpu = 'Ryzen'
            self.ram = 16

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1= student('Yash', 28)
s2= student('Pratteek', 28)
s1.show()