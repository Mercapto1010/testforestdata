from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
class Laptop:
    def process(self):
        print("It's running!")

class Whiteboard:
    def write(self):
        print("It's writing")

class Programmer:
    def work(self,com):
        print("I solve problems")
        com.process()
c1 = Laptop()
c2 = Programmer()
c3 = Whiteboard()
c2.work(c3)