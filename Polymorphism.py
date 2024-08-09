# polymorphism means same function name (but different signatures) being uses for different types. 

# function overloading
# function over-riding

# class Ws:
#     def displayinfo(self,name=''):
#         print("Welcome to "+ name)

# obj=Ws()
# obj.displayinfo() 
# obj.displayinfo("Aakash")

class Ws:
    def displayinfo(self):
        print("Welcome")

class IIP(Ws):
    def displayinfo(self):
        super().displayinfo()
        print("Aakash")

obj=IIP()
obj.displayinfo()