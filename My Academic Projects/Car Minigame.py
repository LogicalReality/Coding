
# This is a simple car engine game.

while True:
    command = input('> Enter a command: ')
    try:
        if 'help' in command.lower():
            # This print function could be better, the indentation that appears of using triple quotes made me come up with this solution.
            print(
                '\n---> Enter one of the following commands: \n\n start - to start the car \n stop - to stop the car \n exit - to exit game\n')       

        elif 'start' in command.lower():
            print('Car started... Ready to go!\n')
        
        elif 'stop' in command.lower():
            print('Car stopped.\n')
        
        elif 'exit' in command.lower():
            break 

        else:
            print("I don't understand that...\n")
    except ValueError:
        print("\nUnexpected Input Error. Use the command [help] if you don't know the commands.")
