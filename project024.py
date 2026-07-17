soma = 0
cont = 0
for c in range(1, 7):
    n1 = int(input('escreva um numero :'))
    if n1 % 2 == 0:
        soma += n1
        cont += 1
print('a soma dos  {} e {}'.format(cont, soma))
