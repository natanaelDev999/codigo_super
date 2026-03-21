numeros = list()
while True:
    numeros.append(int(input('digite um valor:')))
    escolha = ' '
    while escolha not in 'NS':
        escolha = str(input('deseja continuar?: [S/N]')).upper().strip()[0]
    if escolha == 'N':
        break
print(f'o numero de valores e {len(numeros)}')
numeros.sort(reverse=True)
print(numeros)
if 5 in numeros:
    print('o numero 5 esta na lista ')
else:
    print('o numero 5 não esta na lista')