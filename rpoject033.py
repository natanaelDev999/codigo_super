n1 = int(input('escreva um numero:'))
n2 = int(input('escreva outro numero:'))
c = 0
while c != 5:
    print('[1]para somar\n[2]para mutiplicar\n[3]para saber o maior\n[4]para novos numeros\n[5]para sair do progama ')
    c = int(input('qual a sua escolha:'))
    if c == 1:
        print('a soma de {} e {} e {}'.format(n1,n2, n1 + n2))
    elif c == 2:
        print('a multiplicação de {} e {} e {}'.format(n1, n2, n1 * n2))
    elif c == 3:
        if n1 > n2:
            print('{} e maior que {}'.format(n1, n2))
        elif n2 > n1:
            print('{} e maior que {}'.format(n2, n1))
        else:
            print('os numeros são iguais')
    elif c == 4:
        n1 = int(input('escreva um numero:'))
        n2 = int(input('escreva outro numero:'))
    elif c == 5:
        print('saindo do progama')
    else:
        print('opção invalida tente novamente')
print('fim do progama')
