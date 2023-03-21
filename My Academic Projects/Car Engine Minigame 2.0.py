# This is a simple car engine game.
# For this version Car state saved in a variable, and added empty print function to reduce the redundance that was present in 1.0 version

# This line prints a message stating the game's creator.
print('----- LogicalReality -----\n')

# Define a function to print the help message.
def print_help():
    # Print a message to the console that explains the valid commands for the car program.
    print('---> Enter one of the following commands: \n\n start - to start the car \n stop - to stop the car \n exit - to exit game')

# Define a function to start the car engine.
def start_engine():
    # Use the "global" keyword to indicate that we want to modify the global variable "car_engine_is_on".
    global car_engine_is_on
    # Check if the car engine is not already running.
    if not car_engine_is_on:
        # If it isn't, set the variable to True and print a message to the console.
        car_engine_is_on = True
        print('Car started... Ready to go!')
    else:
        # If it is, print a message to the console.
        print('The car engine is already started, what are you doing?!')

# Define a function to stop the car engine.
def stop_engine():
    # Use the "global" keyword to indicate that we want to modify the global variable "car_engine_is_on".
    global car_engine_is_on
    # Check if the car engine is running.
    if car_engine_is_on:
        # If it is, set the variable to False and print a message to the console.
        car_engine_is_on = False
        print('Car stopped.')
    else:
        # If it isn't, print a message to the console.
        print('The car engine is already stopped, what are you doing?!')

# This line prints the intro message
print(''' Welcome, to this simple text minigame
Current State: - The car engine is not started - \n''')


print_help()

# Initialize a variable to keep track of whether the car engine is running.
car_engine_is_on = False

while True:
    # Print a blank line to the console to make the output easier to read.
    print('')
    # Prompt the user for input and convert it to lowercase, then strip any leading or trailing whitespace.
    command = input('> Enter a command: ').strip().lower()
    # Print another blank line to the console.
    print('')
    # Check if the user entered anything.
    if not command:
        # If they didn't, print a message to the console to prompt them to enter a command and continue with the next iteration of the loop.
        print('Please enter a command.')
        continue
    try:
        # Check what command was entered and call the appropriate function.
        if command == 'help':
            print_help()
        elif command == 'start':
            start_engine()
        elif command == 'stop':
            stop_engine()
        elif command == 'exit':
            # If the user entered "exit", break out of the loop to end the program.
            break
        else:
            # If the user entered an invalid command, print a message to the console.
            print("Invalid command. Type 'help' for a list of valid commands.")
    except Exception as e:
        # If an error occurred while executing the command, print an error message to the console.
        print(f"An error occurred: {e}. Type 'help' for a list of valid commands.")