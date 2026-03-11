'''lul = []
for n in range(5):
    lul.append(int(input(f'Type the {n+1}°: ')))
mx = max(lul)
mi = min(lul)
for p, n  in enumerate(lul):
    if n == mx:
        print(f'The MAX value is {n}, in position {p}.')
    if n == mi:
        print(f'The Minimal value is {n}, in position {p}.')
#lul = sorted(lul)
#print(f'The Upper number is: {lul[len(lul)-1]}\nThe Lower number is: {lul[0]}')
ln = []
lr = []
qt = int(input('Type the quantity  of number you want need: '))
for n in range(qt):
    nl = input(f'Type the number {n}: ')
    if nl in ln:
        print(f'The number {nl} is in principal list!')
        lr.append(nl)
    else:
        ln.append(nl)
ln = sorted(ln)
print(f'The list without repeating number: {ln}\nThe list with repeating number: {lr}')'''
