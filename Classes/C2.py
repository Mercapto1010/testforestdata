class computer:
    def __init__(self):
        self.name = "Yash"
        self.age = 20       

    # def update(self):
    #     self.age = 25

    def compare(self,other):
        if self.age == other.age:
            # print("Same!")
            return True
        else:
            # print("Not same!")  
            return False          

c1 = computer()
c2 = computer()
c1.age = 25
if c1.compare(c2):
    print("They are same")

else:
    print("Not same!")
# c1.compare(c2)
# c1.update()
# if c1.age == c2.age:
#     print("They are same")

# else:
#     print("Not same!")    
print(c1.name, c1.age)
print(c2.name, c2.age)