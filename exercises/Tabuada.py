num = 0
while num >= 0 :
    num = int(input(f'Digite o numero: '))
    if num < 0:
        break
    for n in range (11):
        print (f'{num} x {n} = {n*num}')
print('\nEnd.')