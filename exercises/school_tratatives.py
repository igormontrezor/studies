note1 = float(input('Type your firt note: '))
note2 = float(input('Type your second note: '))
average = (note1+note2)/2
if average < 5.0:
    print('Not passed!')
elif average > 5.0 and average < 6.9:
    print('Recovery!')
else:
    print('Aproved!')