from random import randint

t = ["rock", "paper", "scissor"]

computer = t[randint(0,2)]

player = False

while player == False:

    player = input("rock, paper, scissor?")
    if player == computer:
        print("Tie!")
        print ("Computer do", computer)
    elif player == "rock":
        if computer == "paper":
            print("You lose!")
            print ("Computer do", computer)
        else:
            print("You win!")
            print ("Computer do", computer)
    elif player == "paper":
        if computer == "scissor":
            print("You lose!")
            print ("Computer do", computer)
        else:
            print("You win!")
            print ("Computer do", computer)
    elif player == "scissor":
        if computer == "rock":
            print("You lose...")
            print ("Computer do", computer)
        else:
            print("You win!")
            print ("Computer do", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    player = False
    computer = t[randint(0,2)]