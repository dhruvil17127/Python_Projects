import random

choices = ["rock", "paper", "scissors"]

print("Rock,Paper,Scissors Game ✊✋✌️")

while True:

    user = input("Choose rock, paper, scissors (or 'quit' to stop): ").lower()
    if user == 'quit':
        print("Thanks for playing!")
        break
    elif user not in choices:
        print("Invalid choice. Try again!")

    computer = random.choice(choices)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scisoors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")
        
