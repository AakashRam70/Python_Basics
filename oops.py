# class DemoClass:
#  a=10

#  def sumvalue(self):
#     print(20+30)

# demoobject = DemoClass()
# print(demoobject.a)
# demoobject.sumvalue();

# Methods and Constructor 

class DemoObject:
    a =10
    def __init__(self):
        print("constructor")
    def showvalue(self):
       self.c = self.a*self.a
       print(self.c)

    def showvalue1(self,a,b):
        print(a+b)



obj=DemoObject()
obj.showvalue()
obj.showvalue1(10,30)
