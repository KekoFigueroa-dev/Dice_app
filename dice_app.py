#Dice APP -
#Project 7.1 Python Dice Application

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import random

def dice_sides():
    """Ask the user for the number of sides on the dice and return it  """
    sides = int(input("How many sides would you like on your dice? "))
    return sides
    


def dice_number():
    """Ask the user for the number of dice to roll and return it  """
    number = int(input("How many dice would you like to roll? "))
    return number   


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