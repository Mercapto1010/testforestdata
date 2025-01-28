class student:

    schoool = "PPS"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def getschool(cls):
        return cls.schoool   

    @staticmethod
    def info():
        print("Details of students")    
s1 = student(54,45,69)        
s2 = student(25,85,99) 

print(s1.avg())
print(s2.avg())
print(student.getschool())
student.info()