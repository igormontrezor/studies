number =int(input('Type the number: '))
prim = []
for n in range(number):
    if n%3 == 0 or n%2 == 0:
        print(f'Nao: {n}')
    else:
        prim.append(n)
        n1 = (6*n-1)
        n2 = (6*n+1)
        prim.append(n1)
        prim.append(n2)
prim = sorted(prim)
prim = list(set(prim))
print(prim)