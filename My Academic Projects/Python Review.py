#>>>>> Aqui me vuelvo loco repasando Python con Programming With Mosh (Youtube channel)

#>>>>> Practice exercises where made functions to commment them out as needed. This was made this way so I could just practice the ones I want without running the whole code, while using a single file. 

from random import randint, random
import string

def HelloWorld():
    print('\n----- LogicalReality -----\n')

HelloWorld()

#>>>>> Asignar un input del usuario a una variable guardada en memoria, para luego mostrarla en pantalla. Recordar que la función input() da un string, para usar un numero se debe convertir a numero con funcion int() o float() segun sea el caso.

def UserInfo():
    user_name = input(' - Inserta tu nombre >>> ')
    
    user_age = input('\n - Inserte su edad >>> ')

    user_birthyear = 2022 - int(user_age)

    user_color = input('\n - Inserta tu color preferido >>> ')

    print(f'\n---> Hola {user_name.capitalize()} (tienes {user_age} años, nacido en el año {user_birthyear}), te gusta el color {user_color.lower()}.\n')

#UserInfo()

#>>>>>  Ejercicio del peso con If statements.

def WeightConversion():
    user_weight = input(' - Cuanto es tu peso corporal actualmente? >>> ')

    weight_unit = input('\n - Unidad de peso a utilizar: [1] Kg (Kilograms), [2] Libras (Pounds) >>> ')

    if '1' in weight_unit:
        weight_lb = int(user_weight) * 2.204
        print(f'\n ---> Tu peso es de {weight_lb} lb')
    elif '2' in weight_unit:
        weight_kg = int(user_weight) / 2.204
        print(f'\n ---> Tu peso es de {round(weight_kg, 3)} kg')
    else:
            print('\n ---> Por favor insertar solo (1) numero de las opciones propuestas: [1] o [2]')

#WeightConversion()

#>>>>> Ejercicio de la casa.

def HouseCredit():
    house_price = 1000000
    has_good_credit = True

    if has_good_credit:
        down_payment = house_price * 0.10
        print(f' - Your upfront payment for the house is ${down_payment}')
    else:
        down_payment = house_price * 0.20
        print(f' - Your upfront payment for the house is ${down_payment}')

#HouseCredit()

#>>>>> Ejercicio con operadores de comparacion.

def NameLength():
    name = input(" - Ingrese su nombre >>> ")

    if len(name) <= 3:
        print('\n ---> Name must be at least 3 characters long.')

    elif len(name) >= 50:
        print('\n ---> Name can  be maximux 50 characters long')

    else:
        print('\n ---> Name looks good')

#NameLength()

#>>>>> Ejercicio de While Loops. Mientras se cumpla la condicion, el loop se repite. CUIDADO con los loops infinitos
def SimpleLoopAsterisc():   
    i = 1
    while i <= 10:
        print('*' * i)
        i += 1
    print('Done')

#>>>>> Guessing game  con While Loops
def GuessingGame():
    i = 0
    #Settings
    tries = 5
    bottom_number = 1
    ceiling_number = 5
   
   #Random number generator function 
    random_integer =  randint(bottom_number, ceiling_number)

    #Welcome message + explanation
    print(f' - $$$ Guessing Minigame! $$$ - \n')
    print(f' - $ The main goal is to guess a random-chosen integer number between [{bottom_number}] and [{ceiling_number}] $ - \n')

    #The Following line is just for testing purposes
    #print(f' - Random Number: {random_integer} \n')
    
    while i < tries:

        user_input = input(f'Ingrese un numero entre {bottom_number} y {ceiling_number}  (ambos incluidos) >>> ')
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

#GuessingGame()

# For loops

def ForLoop():
    for item in 'LogicalReality':
        print(item)

#ForLoop()

# For loop using a list

def ForLoopList():
    for item in ['Lucas', 'Dustin', 'Eleven']:
        print(item)

#ForLoopList()

def ForLoopRange():
    for item in range(10, 21, 5):
        print(item)

#ForLoopRange()

# The range funcion range(number_excludes_last) or range(start, finish, step), the finishing number is excluded. Use ForLoopRange() to see what I mean.

# Shooping cart exercise
def PriceSum():        
    prices = [10, 20, 30, 120]

    total=0

    for price in prices:
        total += price

    print(f' - Total: {total}') 

#PriceSum()

# Nested Loops example.

def NestedLoop():
    # This list prints a letter F or L with this loop
    number_list_for_F = [5, 2, 5, 2, 2]
    number_list_for_L = [2, 2, 2, 2, 5]
    for x_count in number_list_for_L:
        output = ''
        for i in range(x_count):
            output += 'X'
        print(output)

    
# this could easily be done by multiplying strings, but since in other programming languages doesn't exist such a thing, then we tried another approach.

#NestedLoop()

# Lists in python, larger number in list
def NumberList():
    number_list = [25, 25, 142, 500, 1010, -5]
    highest_number = number_list[0]

    for number in number_list:
        if number > highest_number:
            highest_number = number
    print(f' -  The highest number in the list is: {highest_number}')

#NumberList()

# 2D Lists, list of lists.
def Matrix2DList():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    for row in matrix:
        for item in row:
            print(item)

def NestedElement():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    for row in matrix:
        for item in row:
            print(item)
    print(f'\n - If you want to access a nested element: {matrix[0][2]}')

#NestedElement()

# List methods
def RandomNumberList(HowLong = 10):
    Random_Number_list = []
    for i in range(HowLong):
        Random_Number_list.append(randint(1, 100)) 
    return Random_Number_list
    
def SortedUniquesList(number):
    Random_Number_list = RandomNumberList(number)  
    print(Random_Number_list)
    uniques = []
    for number in Random_Number_list:
        if number not in uniques:
            uniques.append(number)
    Random_Number_list = uniques.copy()

    # print(sorted(Random_Number_list))
    return Random_Number_list 

#SortedUniquesList(25)

# Algorithm FizzBuzz

def FizzBuzz(number):
    if (number % 3 == 0) and (number % 5 == 0) :
        return 'FizzBuzz'
    elif number % 5 == 0:
        return'Buzz'
    elif number % 3 == 0:
        return 'Fizz'
    
    return number

#print(FizzBuzz(randint(1,100)))

# Tuples is a data type that can't be modified, identified by parenthesis.

def TuplesUnpacking():
    coordinates = (1, 2, 3)
    # Unpacking is a very useful feature that can be used with lists and tuples.
    x, y, z = coordinates
    print(x, y, z)

#TuplesUnpacking()

# Phone number exercise

def PhoneExercise():
    my_dictionary = {
        '1': 'One',
        '2': 'Two',
        '3': 'Three',
        '4': 'Four'
    }
    number_string = input(' - Insert a number >>> ')
    output = '\n'

    for i in number_string:
        output += my_dictionary.get(i, "!") + ' '

    print(output)

#PhoneExercise()

def EmojiConverter():
    string = input('> ')
    string_list = string.split(' ')
    EmojiMapping = {
        ':)': '😀',
        ':(': '🙁'
    }
    output = ''
    for item in string_list:
        if item in EmojiMapping:
            output += EmojiMapping.get(item)
        else:
            output += item + ' '
    
    print('\n' + output)

#EmojiConverter()