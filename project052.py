numeros = []
while True:
    numero = int(input('escreva o numero que deseja adicionar a lista:'))
    if numero in numeros:
        print('o numero solicitado ja existe na lista')
    else:
        numeros.append(numero)
        print('o numero adicionado com sucesso')
    escolha = ' '
    while escolha not in 'NS':
        escolha = str(input('deseja continuar o cadastro? ')).upper().strip()[0]
    if escolha == 'N':
        break
numeros.sort()
for num in numeros:
    print(num)