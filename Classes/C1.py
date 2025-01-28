class computer:
    def __init__(self, card, ram):
        self.c = card
        self.r = ram
        # print("I cannt do none about it")
    def config(self):
        print("config is", self.c, self.r)

com1 = computer('i5', 1)
com2 = computer('ryzen', 16)
com1.config()
com2.config()