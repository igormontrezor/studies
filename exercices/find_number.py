import random
num = int(input('Size of draw: '))
lista = []
error = 0
for n in range(num):
    lista.append(n)
    random.shuffle(lista)
while num != lista[0] :
    num = int(input('Type an number for drwan: '))
    if num == lista[0]:
        print(f'\nThe number draw is: {lista[0]}!')
        print(f'You Win!')
    elif num != lista[0]:
        print(f':´(')
        print(f'You Lose!\n Try Again!')
        error += 1
if error <= 2:    
    print(f'\nThe number draw is {num}.\nAnd your attempts they were {error}.\nNICE!!!!!!!!!')
else:
    print(f'\nThe number draw is {num}.\nAnd your attempts they were {error}.\nBAD.')


'''speed = float(input('What is speed: '))
if speed > 80:
    print('You Fined!')
    value = speed - 80
    value = value * 7.0
else:
    value = 0
    print(f'Not Fined.')
print(f'Value of Fine: {value}')

distance = int(input('What the distance in km: '))
price = 0
if distance < 200:
    price = (distance*0.45)
else:
    price = (distance * 0.50)
print(f'The price is: {price}')

year = int(input('Type the year: '))
if year%4 == 0:
    print(f'Bissext: {year}')
else:
    print(f'Not Bissext!')

number = [9,11,5]
if number[0] > number[1] and number[0] > number[2] and number[1] > number[2]:
    print(f'Upper {number[0]}\nMedium: {number[1]}\nLess: {number[2]}')
elif number[0] < number[1] and number [0] < number[2] and number[1] < number[2]:
    print(f'Upper {number[2]}\nMedium: {number[1]}\nLess: {number[0]}')
elif number[2] > number[1] and number[2] > number[0] and number[1] > number[0]:
    print(f'Upper {number[2]}\nMedium: {number[1]}\nLess: {number[0]}')
else:
    print(f'Upper {number[2]}\nMedium: {number[0]}\nLess: {number[1]}')
wage = float(input('Type the wage: '))
if wage > 1250:
    wage += (wage*10)/100
else:
    wage += (wage*15)/100
print(f'The new Wage with plu is: {wage}$!')'''