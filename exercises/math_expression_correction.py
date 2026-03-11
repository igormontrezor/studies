word = input('Type the math expression: ')
ct = 0
ct2 = 0
for w in word:
    if w == '(' or w == ')':
        ct += 1
    if w == '*' or w == '+' or w == '-':
        ct2 += 1

if ct%2 == 0 and ct2%2 == 0:
    print('The expression is ok!')
elif ct%2 != 0:
    print('Erro in expression!\nThe expression dont have total "()".')
elif ct2%2 != 0:
    print('Erro in expression!\nThe expression dont have total "+ or - or *".')