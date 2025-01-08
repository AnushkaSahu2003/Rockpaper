"""
workflow:
1-input(rock paper scissor)
2-computer choice(computer will choose randomly)
3-result print

cases:
A-rock
Rock - Rock = tie
Rock - paper = paper win
Rock - scissor = rock win
B-paper
paper -paper = tie
paper - rock = paper win
paper - scissor = scissor win
C-scissor
scissor - scissor  = tie
scissor - rock = rock win
paper - scissor = scissor win


"""


import random

# List of valid choices
item_list = ["Rock", "Paper", "Scissor"]

# Get user's move and format it properly
user_choice = input("Enter your move (Rock, Paper, Scissor): ").title()

# Validate user input
if user_choice not in item_list:
    print("Invalid choice! Please enter Rock, Paper, or Scissor.")
else:
    # Generate computer's choice
    comp_choice = random.choice(item_list)

    # Display choices
    print(f"User choice: {user_choice}, Computer choice: {comp_choice}")

    # Determine the winner
    if user_choice == comp_choice:
        print("It's a tie!")
    elif user_choice == "Rock":
        if comp_choice == "Paper":
            print("Computer wins!")
        else:
            print("You win!")
    elif user_choice == "Paper":
        if comp_choice == "Scissor":
            print("Computer wins!")
        else:
            print("You win!")
    elif user_choice == "Scissor":
        if comp_choice == "Rock":
            print("Computer wins!")
        else:
            print("You win!")
