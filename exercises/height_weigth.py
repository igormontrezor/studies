weight = float(input('Tape your weight: '))
height = float(input('Tape your height: '))

if height > 100:
    height = height / 100
imc = (weight / (height*height))

if imc < 18.5:
    print(f'Low Weight!\n{imc} IMC')
elif imc >= 18.5 and imc < 25:
    print(f'Nice Weight!\n{imc} IMC')
elif imc >= 25 and imc < 30:
    print(f'Close to obesity!\n{imc} IMC')
else:
    print(f'Obesity!!!\n{imc} IMC')