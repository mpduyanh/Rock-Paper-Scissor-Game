import random
user_name=input("Hi, what's your name? ")
print("Welcome to Rock Paper Scissor,", user_name.capitalize())
won=0
for i in range(5):
    possible_actions=("Rock" , "Paper", "Scissor")
    computer_move=random.choice(possible_actions)
    user_move=input("Make your move: ")
    print("You chose", user_move, "and the computer chose", computer_move)

    if computer_move==user_move:
        print("Draw")
    elif user_move=="Paper" or user_move=="paper":
        if computer_move=="Rock":
            print("You won!")
            won+=1
        else:
            print("You lost!")
    elif user_move == "Rock" or user_move=="rock":
        if computer_move == "Scissor":
            print("You won!")
            won+= 1
        else:
            print("You lost!")
    elif user_move=="Scissor" or user_move=="scissor":
        if computer_move=="Paper":
            print("You won!")
            won+= 1
        else:
            print("You lost!")

if won < 3:
    print("Haha you suck,", user_name.capitalize(), "you only won", won, "times out of 5 games")

if won >= 3:
    print("Wow, you're so good!", "you won", won, "times out of 5 games")