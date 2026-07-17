c = False
cont = soma = divisor = maior  = menor = 0
while not c:
    n1 = int(input('escreva um numero:'))
    cont += 1
    soma += n1
    divisor += 1
    if cont == 1:
        maior = menor = n1
    else:
        if n1  > maior:
            maior = n1
        if n1 < maior:
            menor = n1
    escolha = str(input('quer continuar? [S/N] ')).upper().strip()
    if escolha =='N':
        c = True
    elif escolha == 'S':
        print('ok')
media = soma / divisor
print('a media dos {} e {:.2f} e o maior e {} e o menor {}'.format(cont, media, maior,menor))
print('acabou')


