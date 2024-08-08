#getter
#setter 

class Student:
    def __init__(self):
        self.__name=""

    def getname(self):
        return self.__name

    def setname(self,name):
        self.__name=name

s1=Student()
s1.setname("aakash")
print(s1.getname())
