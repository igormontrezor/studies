import time

qt = int(input('Type quantity of Students: '))
dat1 = list()
dat2 = list()
ct = 0
nl = 0
for n in range(qt):
    print('-----------------------------------------------------')
    name = input('Type the name: ')
    proof1 = float(input('Type the first proof: '))
    proof2 = float(input('Type the second proof: '))
    dat1.append(name.title())
    dat1.append(proof1)
    dat1.append(proof2)
    dat2.append(dat1[:])
    dat1.clear()
print('====================')
print('No. Name      Mediam')
for dt in dat2:
    for n in dt:
        if type(n) == float or type(n) == int:
           ct += n
    print(f'{nl}  {dt[0]} ----- {ct/2:.2f}')
    #print(f'The notes of {dt[0]} are: {dt[1], dt[2]}')
    ct = 0
    nl += 1
while True:
    try:
        print('-----------------------------------------------------')
        p = int(input(f'Which student grade do you want to show? (999 stop): '))  
        if p != 999:
            print(f'Notes {dat2[p][0]} are {dat2[p][1]} and {dat2[p][2]}')
        else:
            break
    except:
        print('Error!')
print('End...')
time.sleep(1)
print('You are welcome! See you!')
