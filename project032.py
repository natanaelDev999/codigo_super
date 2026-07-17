from random import randint
c = False
soma = int(0)
print('vamos jogar, adivinhe que numero escolhi, detalhe entre 0 e 10')
n1 = randint(0,10)
while not c:
    n2 = int(input('escreva o numero que acha que pensei'))
    if n1 == n2:
        print('\033[32mvoce acertou!!! com {} palpites\033[m'.format(soma))
        c = True
    else:
        if n2 < n1:
            print('\033[4;31mmais ERROU\033[m')
            soma += 1
        elif n2 > n1:
            print('\033[4;31mmenos ERROU\033[m')
            soma += 1
