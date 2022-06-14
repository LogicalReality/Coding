#>>>>> Practice excercises where made functions to commment them out as needed

from random import randint, random

def NoobProgrammer():
    print('\n----- LogicalReality -----\n')

NoobProgrammer()

#>>>>> Guessing game  con While Loops
def GuessingGame():
    i = 0
    #Settings
    tries = 5
    bottom_number = 1
    ceiling_number = 5

   #Random number generator function
    random_integer = randint(bottom_number, ceiling_number)

    #Welcome message + explanation
    print(f' - $$$ Guessing Minigame! $$$ - \n')
    print(
        f' - $ The main goal is to guess a random-chosen integer number between [{bottom_number}] and [{ceiling_number}] $ - \n')

    #The Following line is just for testing purposes
    #print(f' - Random Number: {random_integer} \n')

    while i < tries:

        user_input = input(
            f'Ingrese un numero entre {bottom_number} y {ceiling_number}  (ambos incluidos) >>> ')
        try:
            numeric_input = int(user_input)

            if numeric_input == random_integer:
                print('\n ---> Acertaste!\n')
                break
            else:
                i += 1
                print(f'\n ---X Incorrecto. Le quedan {tries - i} intentos.\n')

        except ValueError:
            print('\n - Por favor, ingrese un dato numerico valido\n')

    print(f' - Random Number: {random_integer} \n')


GuessingGame()
