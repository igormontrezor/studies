import random

print('JOKENPO!')
jokenpo = int(input('1 - Stone\n2 - Papper\n3 - Scizor\nType - '))
if jokenpo == 1:
    print(f'You - {jokenpo} - Stone')
elif jokenpo == 2:
    print(f'You - {jokenpo} - Papper')
else:
    print(f'You - {jokenpo} - Scizor')
pc = [1, 2, 3]
lengend = ['Stone', 'Papper', 'Scizor']
random.shuffle(pc)
prize = pc.pop()

if  prize == 1:
    print(f'Pc - {int(prize)} - Stone')
elif prize == 2:
    print(f'Pc - {int(prize)} - Papper')
else:
    print(f'Pc - {int(prize)} - Scizor')

if jokenpo == prize:
    print('Drwa')
elif jokenpo == 1 and prize == 2 or jokenpo == 2 and prize == 3 or jokenpo == 3 and prize == 1:
    print('PC Win!')
elif jokenpo == 1 and prize == 3 or jokenpo == 2 and prize == 1 or jokenpo == 3 and prize == 2:
    print('You Win!')
else:
    print('Error!')
