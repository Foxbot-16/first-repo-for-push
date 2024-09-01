# create a rock paper scissors game in python
import random

# create the variables
player = None
options = ["rock", "paper", "scissors"]

# generate the randonm symbol
computer = random.choice(options)

# get the player input
player = input("Enter your input: ").lower()

# check if the input is valid
if player not in options:
    print("Not a valid input")

# check the winning condtions
if player == computer:
    print("Tie!!")
elif player == "rock" and computer == "scissors":
    print("You win")
elif player == "paper" and computer  == "rock":
    print("You win")
elif player == "scissors" and computer == "paper":
    print("You win")
else:
    print("You lose")

# print the computer choice
print(computer)