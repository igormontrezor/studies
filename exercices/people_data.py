people = int(input('How many people: '))
md = 0
fem = {}
masc = {}
oldm = {}
age = 0
undr = 0

for p in range(people):
    n = input('\nName: ')
    a = int(input('Age: '))
    s = int(input('1-Masculine\n2-Feminine: '))
    print(s)
    
    while s <= 0 or s > 2:
        print('Error!\n1-Masculine\n2-Feminine: ')
        s = int(input('Sex: '))
        if s == 1 or  s == 2:
            break
        
    if s == 1:
       masc.update({n: [a, s]})
       md += a
    
    elif s == 2:
       fem.update({n: [a, s]})
       md += a

for c, m in masc.items():
    if age < m[0]:
        age = m[0]
        oldm = ({c: m[0]})
    else:
        age = age
for f in fem.values():
    if f[0] < 20:
        undr += 1

print(f'The avarage age: {md/people}\nThe Old Man: {oldm}\nHow many womem less 20 years old: {undr}')
