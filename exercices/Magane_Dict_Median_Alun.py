stud = dict()
studs = list()
count = int(input('Type the quantity of students: '))
for s in range(count):
    stud['Name'] = str(input(f'\nType the name of {s+1}° student: '))
    stud['Mediam'] = float(input(f'Type the average of {s+1}° student: '))
    print('')
    if stud['Mediam'] > 7:
        stud['Situation'] = ['Aproved']
    else:
        stud['Situation'] = ['Reproved']
    studs.append(stud.copy())
for i in studs:
    for n, m in i.items():
        print(f'{n}: {m}')
        if n == 'Situation':
            print('')
        if type(m) == int or type(m) == float:
            print(f'Here {m} have one int or float')