# #  METHOD OVERLOADING
# class Student:
#     # def __init__(self,m1,m2):
#     #     self.m1 = m1
#     #     self.m2 = m2

#     def sum(self,a=None,b=None,c=None):
#         s = 0
#         if a != None and b!= None and c!= None:
#              s = a+b+c
#         elif a!= None and b!= None:
#             s = a+b
#         else:
#             s = a

#         return s
    
# s1 = Student()
# x= int(input("enter 1st num. "))
# y= int(input("enter 2nd num. "))
# z= int(input("enter 3rd num. "))
# print(s1.sum(x,y))

# METHOD OVERRIDING
class A:
    def show(self):
        print("in A show")

class B(A):
    # pass
    def show(self):
        print("in B show")
a1 = B()
a1.show()
