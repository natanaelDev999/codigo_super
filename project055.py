numeros = list()
while True:
    numeros.append(int(input('digite um numero:')))
    escolha = ' '
    while escolha not in 'NS':
        escolha = str(input('deseja continuar o cadastro?: [S/N]')).upper().strip()[0]
    if escolha == 'N':
        break
pares = list()
impares = list()
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f'estes são os numeros que você escreveu {numeros}')
if len(pares) > 0:
    print(f'estes são os numeros pares que você escreveu {pares}')
else:
    print('você escreveu nenhum numero par ')
if len(impares) > 0:
    print(f'estes são os numeros impares que você escreveu {impares}')
else:
    print('você escreveu nenhum numero impar')


