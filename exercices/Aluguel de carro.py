import emoji


dias = float(input('Total de dias: '))
km = float(input('Total de kms: '))
preco = float(input('Digite o valor do carro: '))
total = (preco * dias)
desc = float(0)

if dias >= 10 and dias <= 20:
    if km >= 100 and km <= 500:
        final = (preco * dias)
if dias >= 20 and dias <=30:
    if km >= 500 and km <= 1000:
        final = (preco * dias)
elif km <= 200:
    desc = float(input(f'Digite o desconto:' ));
    final = (total - (total*(desc/100)));
else:
    final = (preco * dias);
    
print (f'Valor total a pagar {final}, por {dias} dias e {km} kms.');
print (emoji.emojize(f'Desconto: {total} - {desc}% ::money-mouth_face::'));