#Single Inheritance
#Multilevel Inheritance :- 
#Multiple Inheritance :- You Can Implement more than one class in one class.

class A:
    def dispalyA(self):
        print("Class A")

class B:
    def displayB(self):
        print("Class B")

class C(A,B):
    def displayC(self):
        print("Class C")
    
obj=C()
obj.dispalyA()
obj.displayB()
obj.displayC()