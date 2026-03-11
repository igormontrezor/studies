frase = ('Estudo Python Diário');
print (f'{frase[::2]}');
print (frase.count('o'));
print (frase.count('O'));
print (frase.upper().count('O'));
frase = ('    Estudo Python Diário    ');
print (len(frase.strip()));
frase_ok = (frase.strip());
print (frase_ok);
print (frase_ok.replace('Python', 'Criptos e Mercados'));
print (f'{'Python' in frase}\n{'Curso' in frase}');
print (frase.find('Python')) #posicao inicial da palavra
print (frase.find('python')) #nao existe com P maiusculo, estao mostra -1
print (frase.upper().find('PYTHON')) #Existe na posicao inicial, pois coloquei tudo em maiusculo
print (frase.split()) #criou uma lista das palavras separadas por espaço
frase_div = frase_ok.split() #divide a string pelos espacos entre elas
print (f'{frase_div[2][3]}') # 2 é a palavra Diário e 3 é posicao da letra r na palavra