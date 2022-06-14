# This is a simple car engine game.

#Alternate solution for this minigame.
while True:
    command = input('> Enter a command: ').lower()
    try:
        if command == 'help':
            # This print function could be better, the indentation that appears of using triple quotes made me come up with this solution.
            print(
                '\n---> Enter one of the following commands: \n\n start - to start the car \n stop - to stop the car \n exit - to exit game\n')       

        elif command == 'start':
            print('Car started... Ready to go!\n')
        
        elif command == 'stop':
            print('Car stopped.\n')
        
        elif command == 'exit':
            break
        
        else:
            print("I don't understand that...\n")
    except ValueError:
        print("\nUnexpected Input Error. Use the command [help] if you don't know the commands.")
