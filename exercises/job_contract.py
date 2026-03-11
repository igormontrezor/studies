from datetime import date

dat =dict()
datL = list()
cont = int(input('\nType the number of cadastres: '))
mda = 0
fem = list()
ageplusmda = list()

for c in range(cont):
    print('==========================================')
    dat['name'] = input(f'Type the name {c+1}: ').title()
    dat['sex'] = input('Type the sex (M or F): ').title()
    dat['birth'] = int(input('Type birth year: '))
    dat['age'] = int(date.today().year) - dat['birth']
    dat['job'] = int(input('Type the job inscrition: '))
    dat['ycontract'] = int()
    dat['wage'] = float()
    dat['retirement'] = int()
    if dat['job'] != 0 and dat['age'] > 16:
        dat['ycontract'] = int(input('Type the date of begins the contract: '))
        dat['wage'] = float(input('Type the wage: '))
        if dat['sex'] == 'F':
            dat['retirement'] = (dat['ycontract'] + 30)
        else:
            dat['retirement'] = (dat['ycontract'] + 35)
    else:
        print('The person is underage, they shoudn"t have a contract!')
        dat['job'] = 0
    datL.append(dat.copy())
    if dat['sex'] == 'F':
        fem.append(dat.copy())

for dt in datL:
    print('==========================================')
    print(f'Name: {dt['name']}\nBirth: {dt['birth']}\nAge: {dt['age']}\nSex: {dt['sex']}\nJob: {dt['job']}\nContract: {dt['ycontract']}\nWage: {dt['wage']}\nRetirement: {dt['retirement']}')
    print('==========================================')
    mda += dt['age']

mda = int(mda/len(datL))

for p in datL:
    if p['age'] > mda:
        ageplusmda.append(p)
print('========================END===========================')
print(f'-The people group have: {len(datL)}\n-The median age is: {mda}\n-The womam cadastred is: {[n['name'] for n in fem]}\n-The people upper {mda}: {[m['name'] for m in ageplusmda]} ')
print('========================END===========================')