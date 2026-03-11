import random
import time


game = dict()
champion = list()
print('\n')
p = int(input(f'Type the quantity of players: '))
for pl in range(p):
    key = str(input(f'Type the {pl+1}° name: ')).title()
    value = int(random.randint(1,6))
    game[key] = value
    game = dict(sorted(game.items(), key=lambda item:item[1], reverse=True))

print('\n')
champion = list(game.items())
for i in champion:
    time.sleep(1)
    print('=====================================')
    for i2 in i:
        if type(i2) == int:
            print(f'****({i2})****')
        else:
            print(i2)
print('=====================================')
if champion[0][1] == champion[1][1]:
    print(f'\nPlay again, DRAWN!\n{champion[0][0]} and {champion[1][0]}: {champion[0][1]}')
else:
    print(f'\nThe WINNER is {champion[0][0]}: {champion[0][1]}')