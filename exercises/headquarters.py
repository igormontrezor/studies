ls = list()
ct = pair = sumc3 = 0
ct2 = 3
for n in range(3):
    for j in range(3):
        p = (int(input(f'Type {n, j}: ')))
        ls.append(p)
        if p%2 == 0:
            pair += p
for n in range(1, 4):
    if n == 2:
        maxl2 = sorted(ls[ct:ct2])
        maxl2 = maxl2[n]
    print(f'{ls[ct:ct2]}')
    sumc3 += ls[ct2-1]
    ct += 3
    ct2 += 3
print(f'Total pair typed: {pair}\nSum line 3: {sumc3}\nThe max number line 2: {maxl2}')

'''while ct < 3:
    if ct == 0:
        print(l[ct], l[ct+1], l[ct+2])
    elif ct == 1:
        print(l[ct+2], l[ct+3], l[ct+4])
    elif ct == 2:
        print(l[ct+4], l[ct+5], l[ct+6])  
    ct += 1'''