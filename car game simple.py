started = False
while True:
    initiate = input(">")
    if initiate.upper() == 'HELP':
        print('Start - to start the car')
        print('Stop - to stop the car')
        print('Exit - to quit the game')
    elif initiate.upper() == 'START':
        if started:
            print('Car Already started!!!')
        else:
            started = True
            print('Car started... Ready to Go!')
    elif initiate.upper() == 'STOP':
        if not started:
            print('Car already stopped !!!')
        else:
            started= False
            print('Car stopped...!')
    elif initiate.upper() == 'EXIT':
        print('program terminated...!')
    elif initiate.upper() == 'QUIT':
        break

    else:
        print("Sorry, i didnt understand (-_-)!!")





