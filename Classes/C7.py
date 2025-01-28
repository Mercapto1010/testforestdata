
class Pycharm():
    def execute(self):
        print("Compiling")
        print("Running")

class Myeditor():
    def execute(self):
        print("Spell check")
        print("convention check")
        print("Compiling")
        print("Running")

class Laptop:
    def code(self, ide):
        ide.execute()

# ide = Pycharm()
ide = Myeditor()
lap1 = Laptop()
lap1.code(ide)