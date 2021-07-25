# Python Random & Time Module.
import random
import time


# Dice Roller Function.
def dice_roller():
    while True:
        print("Rolling dice...")
        # The program makes a delay of 1 second.
        time.sleep(1)
        # The program chooses a random number between 1 and 6.
        dice_number = random.randint(1, 6)
        print(f"Your dice number: {dice_number}")
        # If the user doesn't want to use the program again, the loop stops.
        play_again = input("Do you want to roll the dice again? (Yes/No): ")
        if play_again.lower().capitalize() != "Yes":
            break


# Calling The Dice Roller Function.
dice_roller()
