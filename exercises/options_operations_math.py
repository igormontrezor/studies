opc = 0
while opc >= 0 < 6:
    opc = int(input('\nWhat your option: \n[Sum]-1\n[Multiply]-2\n[Upper]-3\n[New Number]-4\n[End]-5\n...'))
    while opc == 4:
        print('Start again...')
        opc = int(input('\nWhat your option: \n[Sum]-1\n[Multiply]-2\n[Upper]-3\n[New Number]-4\n[End]-5\n...'))    
    if opc >= 5:
        if opc == 5:
            print('\n...End...!')
            break
        else:
            print('\nError Number...')
            print('...End!')
            break
    n1 = int(input('\nType the first number: '))
    n2 = int(input('Type the second number: '))
    if opc == 1:
        print(f'\nThe sum is: {n1+n2}')
    elif opc == 2:
        print(f'\nThe multiply is: {n1*n2}')
    elif opc == 3:
        if n1 > n2:
            print(f'\nThe Upper is: {n1} ')
        else:
            print(f'\nThe Upper is: {n2} ')