# Stack is a linear data structure. 
# Stores items in a Last-in/First-Out (LIFO) or First-In/Last-Out (FILO) manner. 

l =[]
while True:
    c=int(
        input('''
1. Push Elements
2. Pop Elements
3. Peek Elements
4. Display Elements
5. Exit
              
''')
    )

    if c==1:
        n=input("Enter the value");
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("Empty Stack")
        else:
            p=l.pop()
            print(p)
            print(l)
    elif c==3:
        if len(l)==0:
            print("Empty Stack")
        else:
            print("Last Stack Value", l[-1])
    elif c==4:
        print("Dispaly Stack", l)
    elif c==5:
        break;
        
             

    