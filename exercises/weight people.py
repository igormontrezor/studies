'''dados = list()
all = list()
while True:
    dados.append(input('Type the Name: '))
    dados.append(int(input('Type the wheigth: ')))
    all.append(dados[:])
    dados.clear()
    cnt = int(input('\nType 1 for continue or 0 for break: '))
    if cnt == 0:
        break
print(f'\nHow many peoples are cadastre: {len(all)}')
for a in all:
    if a[1] >= 100:
        print(f'Upper 80KG: {a[0]}')
    elif a[1] <= 70:
        print(f'Lower 80kg: {a[0]}')'''
num = [[],[]]
for n in range(0,7):
    typen = int(input(f'Type the {n+1}°: '))
    if typen%2 == 0:
        num[0].append(typen)
    else:
        num[1].append(typen)
print(f'The Organized Pair List is: {sorted(num[0])}\nThe Organized Odd List is: {sorted(num[1])} ')