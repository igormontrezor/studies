salario = float(input(f'Digite o valor do salario:  '));
div = float(input(f'Digite o aumento em %: '));
total = float(salario+(salario*(div/100)))
print (f'O antigo salario: {salario}\nAumento de: {div}%\nNovo salário: {total}');