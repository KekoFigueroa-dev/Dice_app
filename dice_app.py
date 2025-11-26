"""
Dice App – Project 7.1 (The Art of Doing)

This script is my version of the "Python Dice Application" from
The Art of Doing Python projects. It simulates rolling any number
of dice with any number of sides, and includes input validation
and other small improvements added by me.

High-level behavior:
- The program welcomes the user and then repeatedly:
    1. Asks how many sides each die should have.
    2. Asks how many dice to roll.
    3. Rolls the requested dice and shows each individual result.
    4. Sums all dice values and displays the total.
    5. Asks the user whether they want to roll again.
- The application continues to run until the user chooses to quit,
  then prints a goodbye message.

Input validation:
- For the number of sides and number of dice, the program:
    - Ensures the user enters a valid whole number.
    - Rejects zero and negative numbers.
    - Re-prompts the user until a valid positive integer is provided.
- This prevents the program from crashing on invalid input and ensures
  that only sensible values are used for dice rolls.

Functions:
- dice_sides()
    Asks the user how many sides each die should have, validates the
    input, and returns a positive integer representing the number of sides.

- dice_number()
    Asks the user how many dice to roll, validates the input, and
    returns a positive integer representing the number of dice.

- roll_dice(sides, number)
    Uses Python's random module to simulate rolling `number` dice,
    each with `sides` sides. Prints how many dice were rolled, prints
    each individual roll, and returns a list containing all dice values.

- sum_dice(dice)
    Takes a list of dice values, computes the total using sum(), and
    prints the total roll value. This function does not return anything.

- roll_again()
    Asks the user if they would like to roll again. Interprets 'y' (case
    insensitive) as continuing, and any other response as stopping.
    Returns a Boolean value (True to keep rolling, False to exit).

Main loop:
- The main part of the script:
    - Prints a welcome message.
    - Uses a Boolean flag to control a while loop.
    - On each loop iteration:
        * Calls dice_sides() and dice_number() to get user choices.
        * Calls roll_dice() to perform and display the rolls.
        * Calls sum_dice() to display the total.
        * Calls roll_again() to decide whether to continue or exit.
    - After the user chooses not to roll again, prints a final
      thank-you and goodbye message.

This version focuses on clear function separation, simple control
flow, and robust user input handling to make the application easier
to use and less error-prone.
"""
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import random

def dice_sides():
    """Ask the user for the number of sides on the dice and return it  """
    while True:
        user_input = input("How many sides should each die have?")
        try:
            sides = int(user_input)
            if sides < 1:
                print("Please enter a positive integer for the number of sides.")
            else:
                return sides
        except ValueError:
            print("Invalid input. Please enter a valid whole number")
   


def dice_number():
    """Ask the user for the number of dice to roll and return it  """
    while True:
        number = (input("How many dice would you like to roll? "))
        try:
            number = int(number)
            if number < 1:
                print("Please enter a positive integer for the number of dice.")
            else:
                return number
        except ValueError:
            print("Invalid input. Please enter a valid whole number")  


def roll_dice(sides, number):
    """Roll the given number of dice with the given number of sides and return the results as a list"""
    dice = []
    print(f"You rolled {number} {sides} sided dice")
    print("\n-----Results-----")
    for i in range(number):
        die = random.randint(1, sides)
        print(f"{die}")
        dice.append(die)
    return dice


def sum_dice(dice):
    """sum all values from the list dice and return the total"""
    print(f"The total value of your dice is: {sum(dice)}")  


def roll_again():
    """Ask the user if they want to roll again and return True/False"""
    choice = input("Would you like to roll again? (y/n) ").lower()
    if choice != 'y':
        roll =  False 
    else:
        roll = True
    return roll  


def reward_flower():
    print("         _____")
    print("       .\'     \'.")
    print("      /  .-\"-.  \\")
    print("     /  /     \\  \\")
    print("     | |  .-.  | |")
    print("  ___| | (   ) | |___")
    print(" /___  \\  `-'  /  ___\\")
    print("     \\  '-----'  /")
    print("      '._______.'")
    print("          | |")
    print("          | |")
    print("          |_|")

# Main Program
print("Welcome to my Python Dice App!")
is_rolling = True
while is_rolling:
    #get user input and number of dice/sides
    d_sides = dice_sides()
    d_number = dice_number()

    #roll and sum the dice
    my_dice = roll_dice(d_sides, d_number)
    sum_dice(my_dice)

    #ask to roll again
    is_rolling = roll_again()


print("Thank you for using my Dice App! Goodbye!")
reward_flower()