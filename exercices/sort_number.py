def sort_number():
    from random import randint


    num = randint(0,100)
    return(num)

num = sort_number()
while True:
    player = int(input('Enter with number: '))
    if num > player:
        if num - player < 5:
            print('Wow, you is close! +')
            continue 
        print('Hot +')
    elif num < player:
        if player - num < 5:
            print('Wow, you is close! -')
            continue
        print('Hot -')
    elif num == player:
        print('You Win!')
        break
    else:
        print('Try Again...')