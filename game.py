# import options for the game
import random
item_list=["rock", "paper", "scissors"]
your_choice = input("Enter your choice = rock, paper, scissors= ")
comp_choice = random.choice(item_list)

print (f"your choice= {your_choice}, computer choice= {comp_choice}")
# conditions for the game
if your_choice   == comp_choice:
    print(" Both chooses same : = It's a tie!")
#conditons for rock
elif your_choice == "rock":  
    if comp_choice == "paper":
        print("Computer wins! Paper covers rock.")
    else:
        print("You win! Rock crushes scissors.")
# conditions for paper
elif your_choice == "paper":
    if comp_choice == "scissors":
        print("Computer wins! Scissors cut paper.")
    else:
        print("You win! Paper covers rock.")
# conditions for scissors
elif your_choice == "scissors":
    if comp_choice == "paper":
        print("You win! Scissors cut paper.")
    else:
        print("Computer wins! Rock crushes scissors.")