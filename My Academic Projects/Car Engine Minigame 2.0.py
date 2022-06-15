# This is a simple car engine game.
# For this version Car state saved in a variable, and added empty print function to reduce the redundance that was present in 1.0 version
print('\n----- LogicalReality -----\n')

print(' - The car engine is not started -')

car_engine_is_on = False

while True:
    print('')
    command = input('> Enter a command: ').lower()
    print('')
    try:
        if command == 'help':
            # This print function could be better, the indentation that appears of using triple quotes made me come up with this solution.
            print(
                '---> Enter one of the following commands: \n\n start - to start the car \n stop - to stop the car \n exit - to exit game')       

        elif command == 'start':
            if not car_engine_is_on:
                car_engine_is_on = True
                print('Car started... Ready to go!')
            else:
                 print('The car engine is already started, what are you doing?!')
        
        elif command == 'stop':
            if car_engine_is_on:
                car_engine_is_on = False
                print('Car stopped.')
            else:
                print('The car engine is already stopped, what are you doing?!')

        elif command == 'exit':
            break
        
        else:
            print("I don't understand that...")
    except ValueError:
        print("Unexpected Input Error. Use the command [help] if you don't know the commands.")
