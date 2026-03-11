peca = float(input(f'Digite o valor da peça:  '));
div = float(input(f'Digite o desconto em %: '));
total = float(peca-(peca*(div/100)))
print (f'O preco original da peca: {peca}\nO preco com desconto de {div}% é: {total}');