import random

def roll_dice():
    return random.randint(1,6)

print("Dice Rolling Simulator 🎲")

while True:
    roll = input("Roll the dice? (yes/no): ").lower()

    if roll == "yes":
        print("You rolled:",roll_dice())
    elif roll == "no":
        print("Thanks for playing!")
        break
    else:
        print("Please type 'yes' or 'no'")
