'''ext = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten')
while True:
    num = int(input('Type the number: '))
    if num >= len(ext):
        num = int(input('Type the number: '))
        print(ext[num])
    
    contin = input('\n1 for continue and 2 for end: ')
    if contin == 2:
        break
champion = ('Fluminense', 'Sao Paulo', 'Gremio', 'Corinthians', 'Internacional', 'Chapecoense', 'Mirassol', 'Bahia', 'Santos', 'Vasco', 'Botafogo', 'Flamengo')
print(f'The five first are: {champion[0:5]}\nThe five last: {champion[6:]}\nOrder teams: {sorted(champion)}\nChape is: {champion.index('Chapecoense')}')

import random


rand = []
for n in range(5):
     rand.append(random.randint(0,1000))
trand = tuple(sorted(rand))

print(f'The tuple is: {trand}\nUpper number: {trand[len(trand)-1]}\nLower number: {trand[0]}')
num = []
pair = []
nine = 0
for n in range(5):
    n = int(input(f'Type the {n+1}° number: '))
    num.append(n)
    if n == 9:
        nine += 1
    if n %2 == 0:
        pair.append(n)

for n in num:
    if n == 3:
        print(f'\nThe number 3 index is: {num.index(n)}.')
    else:
        print(f'\nThe number 3 was not digited.')
        break
num = sorted(tuple(num))
print(f'The tuple: {num}.\nPairs: {tuple(pair)}.\nThe number 9 times: {nine}.')'''

products = ('Beans', 2.50, 'Arroz', 2.00, 'Beef', 15.00, 'Cookie', 1.00, 'Pasta', 1.80)
c = 0
d = 1
while True:
    if d > len(products):
        break
    print(f'{products[c]} - {products[d]}')
    c += 2
    d += 2

l = []
for p in products:
    if type(p) == str:
        l.append(p.lower())
    else:
        continue
print('***********************************************')
q = 0
vowel = ''
for p in l:
    for v in p:
        if v == 'a' or v == 'e' or  v == 'i' or v == 'o' or v == 'u':
            vowel += v
            q += 1
    if q > 0:
        print(f'The word {p} have: {q} vowels, what are, {vowel}')
    else:
        print(f'The word {p} no have vowel.')
    q = 0
    vowel = ''