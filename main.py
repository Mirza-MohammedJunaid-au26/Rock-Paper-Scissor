import random

comp_wins = 0
player_wins = 0

def Choose_Option() :
    user_choice = input("Choose Rock, Papaer or Scissors : ")
    if user_choice in ["Rock","rock","R","r"] :
        user_choice = "r"
    elif user_choice in ["Paper","paper","P","p"] :
        user_choice = "p"
    elif user_choice in ["Scissor","scissor","S","s"] :
        user_choice = "s"
    else:
        print("i don't Understand, try again...")
        Choose_Option()
    return user_choice

def Computer_Option() :
    comp_choice = random.randint(1,3)
    if comp_choice == 1 :
        comp_choice = "r"
    elif comp_choice == 2 :
        comp_choice = "p"
    elif comp_choice == 3 :
        comp_choice = "s"
    return comp_choice

while True:
    print("")
    user_choice = Choose_Option()
    comp_choice = Computer_Option()
    print("")

    if user_choice == "r":
        if comp_choice == "r":
            print("You Choose rock, The Computer Choose rock. !!!you Tied!!!")
        elif comp_choice == "p":
            print("You Choose rock, The Computer Choose paper. !!!you Loose!!!")
            comp_wins += 1
        if comp_choice == "s":
            print("You Choose rock, The Computer Choose scissor. !!!you Win!!!")
            player_wins += 1
    
    elif user_choice == "p":
        if comp_choice == "p":
            print("You Choose paper, The Computer Choose paper. !!!you Tied!!!")
        elif comp_choice == "s":
            print("You Choose paper, The Computer Choose scissor. !!!you Loose!!!")
            comp_wins += 1
        if comp_choice == "r":
            print("You Choose paper, The Computer Choose rock. !!!you Win!!!")
            player_wins += 1
    
    if user_choice == "s":
        if comp_choice == "s":
            print("You Choose scissor, The Computer Choose scissor. !!!you Tied!!!")
        elif comp_choice == "r":
            print("You Choose scissor, The Computer Choose rock. !!!you Loose!!!")
            comp_wins += 1
        if comp_choice == "p":
            print("You Choose scissor, The Computer Choose paper. !!!you Win!!!")
            player_wins += 1

    print("")
    print("Player Wins :" + str(player_wins))
    print("Computer Wins :" + str(comp_wins))
    print("")

    user_choice = input("Do you want to play again? (y/n)")
    if user_choice in ["Yes","yes","Y","y"] :
        pass
    elif user_choice in ["No","no","N","n"] :
        break 
    else :
        break