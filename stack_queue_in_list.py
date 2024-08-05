# Stack is a linear data structure. 
# Stores items in a Last-in/First-Out (LIFO) or First-In/Last-Out (FILO) manner. 

l = []
while True:
    c = int(input(''' 
    1. Push
            2. Pop
            3.Peek
            4.Display
            5.Exit
'''))
    
    if c == 1:
        n = int(input("Enter the value:-"))
        l.append(n)
    elif c == 2:
        if len(l) ==0:
           print("Stack is Empty")
        else:
            p= l.pop()
            print(p)
            print(l)
    elif c == 3:
        print(l[-1])
    elif c == 4:
        print(l)
    elif c == 5:
        break
    else:
        print("Invalid Input")