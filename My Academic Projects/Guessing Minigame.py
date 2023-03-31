# Guessing Minigame with Hot bar

"""Module random for random-chosen integer number"""
from random import randint

print('\n----- LogicalReality -----\n')

# >>>>> Guessing game  con While Loops

# Settings
tries = 5
bottom_number = 0
ceiling_number = 15
hot_bar_aid = True

# Random number generator function
random_number = randint(bottom_number, ceiling_number)

def hot_bar_print(num_input: int) -> None:
    '''
    This function prints a hot bar in the terminal. It indicates how close user's input is to the random number.
    '''
    bar_percent= round(abs(num_input - random_number) / (ceiling_number - bottom_number), 1)
    bar_fill = '#' * int(((1 - (bar_percent)) * 10)) * 2
    bar_empty = '-' * int(bar_percent * 10) * 2 
    hot_bar = ' - Hot bar --> ' + '[' + bar_fill + bar_empty + ']'
    print(f'\n ---X Incorrect. You got {tries - i} tries left.\n')
    if hot_bar_aid:
    # This next if statement is called Ternary Operator
        print(hot_bar, ' Try higher\n' if num_input < random_number else ' Try lower\n')

# The Following line is just for testing purposes
#print(f' - Random Number: {random_number} \n')

while True:
    # Welcome message + explanation
    print(' - $$$ Guessing Minigame! $$$ - \n')
    print(f' - Guess random-chosen integer number between [{bottom_number}] and [{ceiling_number}] - \n')

    i = 0

    while i < tries:

        user_input = input(
            f'Insert a number between {bottom_number} and {ceiling_number} >>> ')
        try:
            numeric_input = int(user_input)

            if numeric_input == random_number:
                print('\n ---> You got it right!\n')
                break
            else:
                i += 1
                if hot_bar_aid:
                    hot_bar_print(numeric_input)

        except ValueError:
            print('\n - Please insert a valid numeric value.\n')

    if i == tries:
        print(f"\nGame over! The random number was {random_number}\n")
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        break
    random_number = randint(bottom_number, ceiling_number)

print("Thanks for playing!")
