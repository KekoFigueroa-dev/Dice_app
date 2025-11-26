# Python Dice App 🎲

This is my version of **Project 7.1: Python Dice Application** from  
_The Art of Doing_ Python projects.

The app simulates rolling a customizable set of dice: the user chooses  
how many sides each die has and how many dice to roll. The program then  
rolls them, shows each result, prints the total, and lets the user decide  
whether to roll again.

I extended the original project with **input validation** and a focus on  
clear function separation, simple control flow, and robust user input  
handling to make the application easier to use and less error-prone.

---

## Overview

### High-level behavior

- The program welcomes the user and then repeatedly:
  1. Asks how many sides each die should have.
  2. Asks how many dice to roll.
  3. Rolls the requested dice and shows each individual result.
  4. Sums all dice values and displays the total.
  5. Asks the user whether they want to roll again.
- The application continues to run until the user chooses to quit,
  then prints a goodbye message.

### Input validation

For both the number of sides and the number of dice, the program:

- Ensures the user enters a valid whole number.
- Rejects zero and negative values.
- Re-prompts the user until a valid positive integer is provided.

This prevents the program from crashing on invalid input and ensures that
only sensible values are used for dice rolls.

---

## Functions and Structure

The script is organized into several focused functions:

### `dice_sides()`

Asks the user how many sides each die should have.

- Validates that the input is a positive integer.
- Keeps asking until it receives valid input.
- Returns the number of sides as an integer.

### `dice_number()`

Asks the user how many dice to roll.

- Validates that the input is a positive integer.
- Keeps asking until it receives valid input.
- Returns the number of dice as an integer.

### `roll_dice(sides, number)`

Uses Python’s `random` module to simulate dice rolls.

- Rolls `number` dice, each with `sides` sides.
- Prints how many dice were rolled and their individual values.
- Returns a list containing all dice values.

### `sum_dice(dice)`

Takes a list of dice values and reports the total.

- Uses Python’s built-in `sum()` to compute the total.
- Prints the total value of the roll.
- Does not return anything (it has a side effect: printing).

### `roll_again()`

Controls whether the application continues.

- Asks the user if they would like to roll again.
- Interprets `'y'` (case-insensitive) as “keep rolling”.
- Treats any other response as “stop”.
- Returns a Boolean (`True` to continue, `False` to exit).

### Main loop

The main part of the script:

1. Prints a welcome message.
2. Sets a Boolean flag to control a `while` loop.
3. On each loop iteration:
   - Calls `dice_sides()` and `dice_number()` to get user choices.
   - Calls `roll_dice()` to perform and display the dice rolls.
   - Calls `sum_dice()` to display the total.
   - Calls `roll_again()` to decide whether to continue or exit.
4. After the user chooses not to roll again, prints a final thank-you
   and goodbye message.

This structure keeps the logic modular and makes the code easier to read,
test, and extend.

---

## Features

- 🎯 Choose **any number of sides** for your dice (e.g. 6, 20, 100…)
- 🎲 Roll **any number of dice** each round
- 📊 See **each individual roll result**
- ➕ See the **total sum** of all dice rolled
- 🔁 Option to **roll again** or **quit** cleanly
- 🧱 **Robust input validation**:
  - Rejects non-numeric input
  - Rejects zero or negative values
  - Re-prompts until valid input is provided

---

## Requirements

- Python 3.x
- Standard library only (no third-party dependencies):
  - `random`

---

## How to Run
# Clone this repository

git clone <YOUR_REPO_URL>

cd <your-repo-name>

# Run the app

python dice_[app.py](http://app.py)


Replace `dice_app.py` with the actual filename of your script and  
`<YOUR_REPO_URL>` / `<your-repo-name>` with your real repo info.

---

## Example Session
Welcome to my Python Dice App!

How many sides should each die have? 20

How many dice would you like to roll? 6

You rolled 6 20 sided dice

-----Results-----

17

20

11

10

19

10

The total value of your dice is: 87

Would you like to roll again? (y/n) n

Thank you for using my the Python Dice App. Goodbye!


---

## Improvements Over the Base Project

Compared to the base “Python Dice Application” project from  
_The Art of Doing_:

- Added **input validation** for:
  - Number of sides per die.
  - Number of dice per roll.
- Improved robustness by handling invalid input without crashing.
- Kept the functions **small and focused** to make the code easier to follow.
- Structured the main loop around a clear Boolean flag for readability.
- Left room for further enhancements like reward systems (e.g. ASCII-art
  mushroom rewards after certain rolls).

---

## Possible Future Enhancements

- Track and display **roll history** across the session.
- Show **statistics** such as average roll or highest single roll.
- Add an ASCII-art **“reward”** (like a mushroom) for special outcomes.
- Convert the script into a **GUI** version (for example, using Tkinter).

---

## Credits

- Base project idea: _The Art of Doing_ Python COURSE  project  
  **“Python Dice Application”** (Project 7.1).
- Implementation, input validation, and additional improvements:  
  **Sergio Figueroa**.
