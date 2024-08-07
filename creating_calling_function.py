
# Creating Function 
def showdata():
    print("welcome to Python")

# Calling Function 
showdata()

# Function Arguments 
def sum(a,b):
    print(a+b)
sum(5,10)

# Default Parameter Value 
def sum(a,b=3):
    print(a+b)
sum(10)

# Return Value 
def square(x):
    return x*x,x*2
s = square(5)
print(s)

