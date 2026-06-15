import random as r
a = ["rock", "paper", "scissors"]
while True:
    computer = r.choice(a)
    user = str(input("enter the options rock, paper or scissors: "))
    if user.lower() != "rock" and user.lower() != "paper" and user.lower() != "scissors": 
        print("not a valid input please enter again")
        continue
    if user.lower() == computer: 
        print(f"tie computer chose {computer} and user chose {user}")
    elif user.lower() == "rock": 
        if computer == "scissors":
            print("you won!")
        else:
            print("you lost")
    elif user.lower() == "scissors": 
        if computer == "paper":
            print("you won!")
        else:
            print("you lost")
    elif user.lower() == "paper": 
        if computer == "rock":
            print("you won!")
        else:
            print("you lost")
    g = str(input("do you wish to contine?: "))
    if g.lower() == "yes": 
        continue
    elif g.lower() == "no":
        break
    else:
        print("please enter a valid input(yes or no)")
        break