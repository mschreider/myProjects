import random

while True:
    computer = random.choice(["rock", "paper", "scissors"])
    guess = input("Rock, paper or scissors? ")
    if computer == guess:
        print("Go again")
    elif (computer == "rock" and guess == "paper") or (computer == "paper" and guess == "scissors") or (computer == "scissors" and guess == "rock"):
        print("You win!")
        
    else:
        print("You lose")


