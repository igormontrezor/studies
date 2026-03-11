house = float(input('What is the house value? '))
wage = float(input('What is the wage? '))
years = int(input('How many years? '))
max = ((30/100)*wage)
y = -1

for x in range(years+1):
    if x%4 == 0:
       y += 1

years2 = (years*12) + (y/12)
provision = (house/years2)

if provision < max:
    print(f'\nYour max discount is {max}, dont ultrapasssed 30%.\nThe provision is: {provision}$\nAproved!!!')
else:
    print(f'\nYour max discount is {max}, ultrapassed 30%.\nThe provision is: {provision}$ o\nNot Aproved.')