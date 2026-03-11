from datetime import date

year = int(input('Type your birth year: '))
dat = int(date.today().year)
print(dat)
if (dat - year) < 9:
    print('Child back 9!') 
elif (dat - year) > 9 and (dat - year) <= 14:
    print('Child 9 to 14!')
elif (dat - year) > 14 and (dat - year) <= 19:
    print('Adolescent!')
elif (dat - year) > 19 and (dat - year) <= 30:
    print('Experient!')
else:
    print('Master!')