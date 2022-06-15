# Get rid of annoying pylint message
# pylint: disable=C0103

"""Module random for random-chosen integer number"""
from random import randint

print('\n----- LogicalReality -----\n')

# >>>>> Guessing game  con While Loops
i = 0
# Settings
tries = 5
bottom_number = 1
ceiling_number = 5

# Random number generator function
random_integer = randint(bottom_number, ceiling_number)

# Welcome message + explanation
print(' - $$$ Guessing Minigame! $$$ - \n')
print(f' - Guess a random integer number between [{bottom_number}] and [{ceiling_number}] - \n')

# The Following line is just for testing purposes
# print(f' - Random Number: {random_integer} \n')

while i < tries:

    user_input = input(
        f'Insert a number between {bottom_number} y {ceiling_number}  (both included) >>> ')
    try:
        numeric_input = int(user_input)

        if numeric_input == random_integer:
            print('\n ---> You got it right!\n')
            break
        else:
            i += 1
            print(f'\n ---X Incorrect. You got {tries - i} tries left.\n')

    except ValueError:
        print('\n - Please insert a valid numeric value.\n')

print(f' - Random Number: {random_integer} \n')
