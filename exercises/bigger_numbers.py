n1 = int(input('Type the first number: '))
n2 = int(input('Type eht second number: '))

if n1 > n2:
    print(f'Number 1: {n1} bigger than Number 2: {n2}')
elif n2 > n1:
    print(f'Number 2: {n2} bigger than Number 1: {n1}')
else:
    print(f'The two number are same: {n1} = {n2}')