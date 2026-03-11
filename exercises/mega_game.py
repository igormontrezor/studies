import random
import time
print('\nGame Mega-Sena\n')
premium = list()
games = list()
qt = int(input(f'Type quantity of games: '))
tot = 1
while tot <= qt:
    cont = 0
    while True:
        num = random.randint(1,60)
        if num not in premium:
            premium.append(num)
            cont += 1
        if cont >= 6:
            break
    premium.sort()
    games.append(premium[:])
    premium.clear()
    tot += 1

for id, it in enumerate(games):
    print(f'\nGenerating the game...{id+1}')
    time.sleep(1)
    print(f'{it}')
    
print('\nEnd Generating.\nGood Luck!')
