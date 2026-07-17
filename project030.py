somaidade = 0
maior = 0
nome_ = ''
totf = 0
for c in range(1,5):
    print('=--=--=--=--=--={} pessoa =--=--=--=--=--='.format(c))
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('sexo M/F:')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maior = idade
        nome_ = nome
    if sexo in 'Mm' and idade > maior:
        maior = idade
        nome_ = nome
    if sexo in 'Ff' and idade < 20:
        totf += 1
mediaidade = somaidade / 4
print('a media de idade e {:.1f} '.format(mediaidade))
print('o homem mais velho se chama {}'.format(nome_))
print('a quantidade de mulheres menores de 20 e {}'.format(totf))