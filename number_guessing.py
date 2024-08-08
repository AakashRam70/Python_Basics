import random

number = random.randrange(1,9)
User = int(input("Enter Any Number Between 1 to 9 :-"))

while True:
    if User >= 10:
        print("Invalid Input")
        break
        
    elif number > User :
        print("You Generate number is too Low")
        print("Computer generated Number is:-", number)
        print("User generated Number is:-", User)
    
    elif number < User :
        print("You Generate number is too High")
        print("Computer generated Number is:-", number)
        print("User generated Number is:-", User)
    
    elif number == User :
        print("You Generate number is same as computer")
        print("Computer generated Number is:-", number)
        print("User generated Number is:-", User)


        