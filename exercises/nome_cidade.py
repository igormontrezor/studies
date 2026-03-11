cidade = input('Digite o nome da cidade: ')
cidade = cidade.title()
cidade = cidade.split()
if cidade[0] == 'Santos':
    print ({f'A cidade {cidade} começa com {cidade[0]}.'})
print (cidade)

nomes = input('Digite seu nome: ')
nomes = nomes.title()
nomes = nomes.split()
for nome in nomes:
    print(nome)
    if nome == 'Montrezor':
        print(f'Seu nome tem {nome}!')

letras = input('Digite a palavras: ')
letras = letras.upper()
letra_find = 'A'
positions = [l for l , char in enumerate(letras) if char == letra_find ]
print (positions)
a = 0
for letra in letras:
    if letra == letra_find:
        a += 1
print(f'A letra a aparece: {a}x')

nome = input ('Digite o nome completo: ')
nomes = nome.title().split()
limit = (len(nomes) - 1)
for nome in nomes:
    if nome == nomes[0]:
            print(nomes[0])            
    if nome == nomes[limit]:
            print(nomes[limit])