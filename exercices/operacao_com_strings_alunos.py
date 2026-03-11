qt = int((input('Digite a quantidade de nomes: ')));
nomes = [];
for n in range(qt):
    nome = (input(f'Digite o {n+1} nome: '));
    nomes.append(nome);
for ns in range (len(nomes)):
    nome = nomes [ns];
    nome_s = (nome.split());
    print (f'Nome {ns+1}: {nome}');
    print (f'Maiusculo: {nome.upper()}');
    print (f'Minusculo: {nome.lower()}');
    print (f'Quantidade de Letras:{len(nome)}');
    for ns2 in nome_s:
        if ns2 == nome_s[0]:
            print (ns2);
            print (len(ns2))
    