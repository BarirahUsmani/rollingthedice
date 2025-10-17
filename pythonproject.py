import random

print("🎲 Welcome to the Dice Rolling Simulator! 🎲")

while True:
    input("Press Enter to roll the dice...")

    dice = random.randint(1, 6)
    print(f"\nYou rolled a {dice}!\n")

    choice = input("Roll again? (y/n): ").lower()
    if choice != 'y':
        print("Thanks for playing!")
        break
