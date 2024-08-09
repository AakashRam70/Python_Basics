# Method overloading is one concept of Polymorphism.
# It comes under the elements of OOPS.
# It is workd in the same method names and different arguments.
# Arguments differnet will be based on a number of arguments and types of arguments.


# method overloading 
class Area:
    def find_area(self,a=None,b=None):
        if a!=None and b!=None :
            print("Area if Rectange is :-", a*b)

        elif a!=None:
            print("Area of Square is:-", a*a)

        else:
            print("Nothing is There..")

obj=Area()
obj.find_area()
obj.find_area(2)
obj.find_area(3,5)

# Method overriding 
# Method Overriding is the method having the same name with the same arguments. 
# It is Implemented with inheritance also 
# It mostlly used for memory reducing processes. 

class A:
    def showData(self):
        print("I am in class A")

class B(A):
    def showData(self):
        print("I am in class B")

obj=B()
obj.showData()