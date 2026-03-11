from datetime import date
high = 0
low = 0
alun = int(input('How many students: '))
years = []
for a in range(alun):
    years = int((input(f'Year of student {a+1}: ')))
    if int(date.today().year) - years   >= 18:
        print(f'Student {a} > 18')
        high += 1
    else:
        print(f'Student {a} < 18')
        low += 1
print(f'Highest 18: {high}\nLowest 18: {low}')
