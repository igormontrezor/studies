import math
import random
alun = []
for a in range(4):
    a = input(f'Digite o nome do {a} Aluno: ');
    alun.append(a)
print (f'A lista de nomes é {alun}\n');
ord = sorted(alun)
print(f'Ordem alfabetica{ord}')
random.shuffle(alun)
print (f'A ordem sorteada: {alun}');
print(f'O aluno sorteado foi: {random.choice(alun)}')