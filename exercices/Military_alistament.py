from datetime import date

birth = int(input('Type your birth year: '))
birth = int(date.today().year - birth)
if birth < 18:
    print(f'Early much!\nMissing {birth} years, for the date of alistament.')
elif birth > 18:
    print(f'Too late!\nPassed {birth} day of your alistament!')
else:
    print('It´s time!')