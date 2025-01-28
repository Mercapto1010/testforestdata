#----------------------------------------INHERITANCE----------------------------------------

class A:  #Grandparents

    def __init__(self):
      print("init of A")

    def feature1(self):
        print("Feature 1-A is working")
    
    def feature2(self):
        print("Feature 2 is working")

class B: #Parents

    def __init__(self):
      
      print("init of B")

    def feature1(self):
        print("Feature 1-B is working")
    
    def feature4(self):
        print("Feature 4 is working")

class C(A,B): #Child

    def __init__(self):
        super().__init__()
        print("init of C")

    def feature5(self):
        print("Feature 5 is working")
    
    def feature6(self):
        print("Feature 6 is working")

a1 = C()
a1.feature1()
