name = input(f'Digite seu nome: ');
notas = []
for num in range(3):
    nota = float(input(f'Digite a nota {num+1}: '));
    notas.append(nota);
    
total = sum(notas);
print(f'Total: {total} ');
print (f'Media Final: {total/int(len(notas))}');