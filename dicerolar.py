import random
print("Welcome to the Dice Roller Game!")   
while True:
    input("Press Enter to roll the dice...")
    dice_roll = random.randint(1, 6)  
    print(f"You rolled a {dice_roll}!")
    play_again = input("Do you want to roll again? (yes/no): ")
    if play_again.lower() != "yes":
        print("Thanks for playing! Goodbye!")
        break
    