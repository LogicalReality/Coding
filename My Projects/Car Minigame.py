
program_on_check = True

while program_on_check:

    command = input('> ')

    try:
        if 'help' in command.lower():
            print('\n---> Enter one of the following commands:\n')
            print('start - to start the car')
            print('stop - to stop the car')
            print('exit - to exit game\n')        

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
