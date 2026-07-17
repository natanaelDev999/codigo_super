from random import randint
print('par ou impar')
vitorias = 0
while True:
    n1 = int(input('escreva sua escolha:'))
    computador = randint(0,10)
    a = n1 + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('qual a sua escolha?: P/I')).upper().strip()[0]
    print(f'você jogou {n1} e o jogou {computador} a soma foi {a}')
    if escolha == 'P':
        if a % 2 == 0:
            print('foi par você ganhou')
            vitorias += 1
        else:
            print(f'deu impar você perdeu com {vitorias} vitorias')
            break
    elif escolha == 'I':
        if a % 3 == 0:
            print('foi impar você ganhou')
            vitorias += 1
        else:
            print(f'foi par você perdeu com {vitorias} vitorias')
            break
