import sys
from random import choice, randint
from time import sleep
print('-------\033[31madventure/\033[m\033[36mgame rpg\033[m---------')
n = input('crie seu nome:')
c = input('escolha sua classe:\033[4;34mguerreiro\033[m,\033[4;35mmago\033[m,\033[4;32mfeiticeiro\033[m ou \033[4;37mpaladino\033[m:')
print('seja bem vindo a este mundo de magia dragões e masmorras {}  {}'.format(c, n))
print('este mundo e assolado por monstros você e a ultima e unica luz para este mundo')
print('\033[31m--=--=--=--=--=--=--=-=\033[36mcomeça aqui sua aventura\033[m\033[31m-=--=--=--=--=--=--=--=\033[m')
print('você estava a caminho de \033[4;36mswordkill\033[m lugar onde o mal era muito forte mas seu navio e naufragado por um grande monstro  ')
print('você então acorda em uma praia ao seu lado ve seu capitão morrendo dizendo "{} va e derrote o grande \033[31mpingu maligno\033[m" e então morre'.format(n))
print('agora você esta em uma estrada quando um duende nivel 1  aparece da mata')
sleep(15)
print('começa agora a batalha o dado foi jogado')
opcoes = [1, 2, 3, 4, 5, 6, ]
escolha = choice(opcoes)
print(f'o dado caiu no:{escolha}')
if escolha >= 3:
    g = str(input('digite  o golpe ou magia que ira desferir:'))
    p = 1
    print(' otimo  você desferiu o \033[31m{}\033[m no duende que cai morto e assim você consegue {} ponto'.format(g, p))
    print(' agora você caminha com mais cuidado')
    print('logo aparece uma aranha nivel 1 gigante')
    print('a batalha começou o dado foi jogado:')
    sleep(5)
else:
    print('\033[4;31mfim do jogo:tente de novo\033[m')
    sys.exit()
opcoe = [1, 2, 3, 4, 5, 6,]
esccola = choice(opcoe)
print(f'o dado caiu no :{esccola}')
if esccola >= 3 :
    g1 = str(input('digite  o golpe ou magia que ira desferir:'))
    p1 = 1
    print(' otimo você desferiu o \033[31m{}\033[m na aranha que cai morta agora você tem mais {} ponto assim você tem {} pontos'.format(g1, p1,2))
    print('você continua a andar')
    print('e no topo de um monte ao longe ve um castelo que você sente que e ali que encontrara o grande \033[31mpingu maligno\033[m')
else:
    print('\033[4;31mfim de jogo:tente novamente\033[m')
    sys.exit()
print('logo você prossegue seu caminho ate o castelo')
print('\033[34mviagem ...\033[m')
sleep(5)
print('\033[4;31m-=--=--=--=--=--=--= a frente do castelo =--=--=--=--=--=--=--=\033[m')
print('\033[41mvocê exita em entrar mas assim mesmo adentra a escuridão nada vivo alem de você se move \033[m \n ossos humanos ou não se encontrevam esmagados\033[m')
print('logo se encontra em uma grande sala escura então você ouve algo a suas costas e encontra com o grande \033[4;31mpingu maligno\033[m')
print('a batalha começou essa sera sua \033[4;31multima batalha!\033[m o dado foi jogado e sera um de 20')
sleep(3)
escolkk = randint(1, 20)
print('o dado caiu no {}'.format(escolkk))
if escolkk >=10:
    print('otimo')
    nt = input('escreva que golpe ou ataque ira desferir:')
    print('otimo você de um {} no \033[31mpingu maligno\033[m que perde um pouco de vida mas continua forte'.format(nt))
    print('o dado foi novamente jogado')
    sleep(3)
    nh = randint(1, 20)
    print('o dado caiu no {}'.format(nh))
    if nh >=10:
        print('otimo')
        g7 = input('escreva o golpe ou magia que ira desferir:')
        print('otimo você de um {} no \033[31mpingu maligno\033[m que fica um pouco fraco'.format(g7))
        print('o dado foi novamente jogado')
        sleep(3)
        ny = randint(1, 20)
        if ny >=10:
            print('otimo')
            g4 = input('escreva o golpe ou magia que ira desferir:')
            print('otimo você da um {} no \033[31mpingu maligno\033[m que cai morto assim você consegue +3 pontos ficndo com {}'.format(g4,(2 +3)))
            print('\033[4;33m=--=--=--=--=--=--=--=--= fim =--=--=--=--=--=--=--=--=\033[m')
    elif nh == 20:
        print('parabens !!!')
        g9 = input('que golpe ou magia ira desferir:')
        print('otimo você da um {} no \033[31mpingu maligno\033[m que cai morto assim você consegue +3 pontos e assim fica {}'.format(g9, (3 + 2)))
        print('\033[4;33m=--=--=--=--=--=--= fim =--=--=--=--=--=--=--=\033[m')
    else:
        print('\033[31mfim de jogo: tente novamente\033[m')
        sys.exit()
elif escolkk == 20:
    print('parabens !!!')
    ghl = input('que golpe ou magia ira desferir:')
    print('otimo você da um {} no pingu maligno que cai morto assim você consegue +3 pontos e assim você fica com {} '.format(ghl, (3 + 2)))
    print('\033[4;33m=--=--=--=--=--=--=--=--=--=--= fim =--=--=--=--=--=--=--=--=--=--=\033[m')
else:
    print('\033[31mfim de jogo:tente novamente\033[m')
    sys.exit()