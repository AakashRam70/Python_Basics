import random

list = ["rock", "paper", "scissor"]

while True:
    ccount = 0
    ucount = 0
    uc = int(input('''
Game Start...
1. Yes
2. No | Exit               
'''))
    if uc == 1:
        for a in range(1, 6):
            userInput = int(input('''
1. Rock
2. Paper
3. Scissor
'''))
            if userInput == 1:
                uchoice = "rock"
            elif userInput == 2:
                uchoice = "paper"
            elif userInput == 3:
                uchoice = "scissor"
            Cchoice = random.choice(list)
            if Cchoice == uchoice:
                print("Computer Value:", Cchoice)
                print("User Value:", uchoice)
                print("Game Draw")
                ucount += 1
                ccount += 1
            elif (uchoice == 'rock' and Cchoice == "scissor") or (uchoice == "paper" and Cchoice == "rock") or (uchoice == "scissor" and Cchoice == "paper"):
                print("Computer Value:", Cchoice)
                print("User Value:", uchoice)
                print("You Win")
                ucount += 1
            else:
                print("Computer Value:", Cchoice)
                print("User Value:", uchoice)
                print("Computer Win")
                ccount += 1
        if ucount == ccount:
            print("Game Draw")
            print("Computer Count:", ccount)
            print("User Count:", ucount)
        elif ucount > ccount:
            print("You Win")
            print("Computer Count:", ccount)
            print("User Count:", ucount)
        else:
            print("Computer Win")
            print("Computer Count:", ccount)
            print("User Count:", ucount)
    else:
        break
