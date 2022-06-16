# Reviewing Python: Programming With Mosh (Youtube channel)
# Practice exercises where made functions to commment them out as needed. This was made this way so I could just practice the ones I want without running the whole code, while using a single file.

from random import randint, random
import string
import string


def hello_world():
    print('\n----- LogicalReality -----\n')


hello_world()

# Remember that input() function returns a string, if you wanna convert it into a numeric value you can use int() o float().


def user_info():
    user_name = input(' - Inserta tu nombre >>> ')
    user_age = input('\n - Inserte su edad >>> ')
    user_birthyear = 2022 - int(user_age)
    user_color = input('\n - Inserta tu color preferido >>> ')
    print(f'\n---> Hola {user_name.capitalize()} (tienes {user_age} años, nacido en el año {user_birthyear}), te gusta el color {user_color.lower()}.\n')


# user_info()

#  Ejercicio del peso con If statements.


def weight_conversion():
    user_weight = input(' - Cuanto es tu peso corporal actualmente? >>> ')

    weight_unit = input(
        '\n - Unidad de peso a utilizar: [1] Kg (Kilograms), [2] Libras (Pounds) >>> ')

    if '1' in weight_unit:
        weight_lb = int(user_weight) * 2.204
        print(f'\n ---> Tu peso es de {weight_lb} lb')
    elif '2' in weight_unit:
        weight_kg = int(user_weight) / 2.204
        print(f'\n ---> Tu peso es de {round(weight_kg, 3)} kg')
    else:
        print(
            '\n ---> Por favor insertar solo (1) numero de las opciones propuestas: [1] o [2]')


# weight_conversion()

# Ejercicio de la casa.


def house_credit():
    house_price = 1000000
    has_good_credit = True

    if has_good_credit:
        down_payment = house_price * 0.10
        print(f' - Your upfront payment for the house is ${down_payment}')
    else:
        down_payment = house_price * 0.20
        print(f' - Your upfront payment for the house is ${down_payment}')


# house_credit()

# Comparison operators exercise


def name_length():
    name = input(" - Insert your name >>> ")
    if len(name) <= 3:
        print('\n ---> Name must be at least 3 characters long.')

    elif len(name) >= 50:
        print('\n ---> Name can  be maximux 50 characters long')
    else:
        print('\n ---> Name looks good')


# name_length()

# While Loop exercise. While a certain boolean expression is true, the loop is executed. BEWARE with infinite loops.


def simple_loop_asterisc():
    i = 1
    while i <= 10:
        print('*' * i)
        i += 1
    print('Done')


# >>>>> Guessing game using While Loops


def guessing_game():
    i = 0
    # Settings
    tries = 5
    bottom_number = 1
    ceiling_number = 5

   # Random number generator function
    random_integer = randint(bottom_number, ceiling_number)

    # Welcome message + explanation
    print(f' - $$$ Guessing Minigame! $$$ - \n')
    print(
        f' - $ The main goal is to guess a random-chosen integer number between [{bottom_number}] and [{ceiling_number}] $ - \n')

    # The Following print call is just for testing purposes
    #print(f' - Random Number: {random_integer} \n')

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


# guessing_game()

# For loops


def for_loop():
    for item in 'LogicalReality':
        print(item)

# for_loop()

# For loop using a list


def for_loop_list():
    for item in ['Lucas', 'Dustin', 'Eleven']:
        print(item)

# for_loop_list()


def for_loop_range():
    for item in range(10, 21, 5):
        print(item)


# for_loop_range()

# The range funcion range(number_excludes_last) or range(start, finish, step), the finishing number is excluded. Use for_loop_range() to see what I mean.

# Shooping cart exercise


def price_sum():
    prices = [10, 20, 30, 120]
    total = 0
    for price in prices:
        total += price
    print(f' - Total: {total}')


# price_sum()

# Nested Loops example. Prints a letter.


def nested_loop():
    number_list_for_F = [5, 2, 5, 2, 2]
    number_list_for_L = [2, 2, 2, 2, 5]
    for x_count in number_list_for_L:
        output = ''
        for i in range(x_count):
            output += 'X'
        print(output)


# nested_loop()
# This could easily be done by multiplying strings, but since in other programming languages doesn't exist such a thing, then we tried another approach.

# Lists in python, this function figures out which is the larger number in list
def number_list():
    number_list = [25, 25, 142, 500, 1010, -5]
    highest_number = number_list[0]

    for number in number_list:
        if number > highest_number:
            highest_number = number
    print(f' -  The highest number in the list is: {highest_number}')


# number_list()

# 2D Lists, list of lists.


def matrix_list():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    for row in matrix:
        for item in row:
            print(item)

# Accessing an element in a 2D List.


def nested_element():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    for row in matrix:
        for item in row:
            print(item)
    print(f'\n - If you want to access a nested element: {matrix[0][2]}')


# nested_element()

# Usage of some List methods


def random_number_list(HowLong=10):
    Random_Number_list = []
    for i in range(HowLong):
        Random_Number_list.append(randint(1, 100))
    return Random_Number_list

# Returns a sorted list of unique random numbers. It filters out the repeated numbers.


def sorted_uniques_list(number):
    random_list = random_number_list(number)
    print(random_list)
    uniques = []
    for number in random_list:
        if number not in uniques:
            uniques.append(number)
    random_list = uniques.copy()
    # print(sorted(random_list))
    return random_list


# sorted_uniques_list(25)

# Algorithm FizzBuzz
def fizz_buzz(number):
    if (number % 3 == 0) and (number % 5 == 0):
        return 'FizzBuzz'
    elif number % 5 == 0:
        return'Buzz'
    elif number % 3 == 0:
        return 'Fizz'
    return number


# print(fizz_buzz(randint(1,100)))

# Tuples is a data type that can't be modified, identified by parenthesis.
def tuples_unpacking():
    coordinates = (1, 2, 3)
    # Unpacking is a very useful feature that can be used with lists and tuples.
    x, y, z = coordinates
    print(x, y, z)


# tuples_unpacking()

# Phone number exercise


def phone_exercise():
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


# phone_exercise()

# Emoji converter: this function converts a string that can be converted into emoji if it is found in the dictionary.


def emoji_converter():
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


# emoji_converter()

# This Version has less code.


def emoji_converter2():
    string = input('> ')
    string_list = string.split(' ')
    EmojiMapping = {
        ':)': '😀',
        ':(': '🙁'
    }
    output = ''
    for item in string_list:
        output += EmojiMapping.get(item, item) + ' '
    print('\n' + output)


# emoji_converter2()

# --------------- Object Oriented Programming -------------------

# Class atributes and methods. Remember that every object is a unique instance of its class.
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'\n - Hi, my name is {self.name}\n')


person1 = Person('Tyronne')
print(person1.name)
person1.talk()

# Class inheritance: new classes can inherit attributes and methods from parents classes.


class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    # Pass is used to just skip this line, don't leave a class empty.
    pass


class Cat(Mammal):
    pass


cat1 = Cat()
cat1.walk()
dog1 = Dog()
dog1.walk()


class Dog2(Mammal):
    def bark(self):
        print('Woof Woof')


class Cat2(Mammal):
    def meow(self):
        print('Meow Meow')


cat2 = Cat2()
cat2.meow()
dog2 = Dog2()
dog2.bark()
