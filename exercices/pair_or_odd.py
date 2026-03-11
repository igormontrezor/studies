import random

pair = odd = vict = 0
lis = []
for n in range(0, 11):
    lis.append(n)
while vict >= 0:
    pair_odd = int(input(f'\nPAIR 1:\nODD 2: '))
    if pair_odd < 0 or pair_odd > 2:
        print('Error! 1 or 2')
        break
    np = int(input('\nTyped the number: '))
    if np > 10:
        print(f'Error {np} > 10!!!')
        break
    random.shuffle(lis)
    pc = lis[0]
    if pair_odd == 1:
        pair = (np+pc)
        if pair%2 == 0:
            print(f'\nYou: {np}\nPc: {pc}\nTotal: {np+pc}\n\nYou Win!!')
            vict += 1
        else:
            print(f'\nYou: {np}\nPc: {pc}\nTotal: {np+pc}\n\nYou Lose!!')
            break
    elif pair_odd == 2:
        print('Odd!')
        odd = (np+pc)
        if odd%2 != 0:
            print(f'\nYou: {np}\nPc: {pc}\nTotal: {np+pc}\n\nYou Win!!')
            vict += 1
        else:
            print(f'\nYou: {np}\nPc: {pc}\nTotal: {np+pc}\n\nYou Lose!!')
            break
print(f'\nYour victoris are: {vict}')
