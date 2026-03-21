import os
import time
#notas:tempo necessario para ser concluido foi 3 dias, ajudas externas:pesquisa de como ler de trás para frente uma lista, como usar loop para mudar certa parte de uma ...
#matrix ,erros ajeitados por entidades externas 1 o da matrix com loop na atualização do monstro, tipo de pixel 0 = céu,1 = terra,3 = espada,8 = monstro
#marcador de direcao
direcao = ['sul','leste','norte','oeste']
#matrix para visualização
tela = [[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],]
#variaveis de comunicação do ''front-end''
print('tipo de pixeis para compreensão:\n\033[34m0 = céu\033[m,\n\033[32m1 = terra\033[m,\n\033[37m3 = espada\033[m,\n\033[31m8 = monstro\033[m')
vida_inimigo =  25
vida = 100
sit = False
c = 0
dir = 0
ata = False
#loop do jogo acaba ao o jogador morrer ou sair
while True:
    #faz a preparção da matrix para o jogo
    if c == 0:
        print(f'-{direcao[dir]: >9}{"-": >9}')
        for linha in tela[3:]:
            del(linha[:])
            for ck in range(0,10):
                linha.append(1)
            l = 2
            l2 = 6
            for ch in range(0,4):
                tela[l][l2] = 3
                l += 1
                l2 += 1

        for l in tela:
            for lm in l:
                print(lm,end=' ')
            print()
            time.sleep(0.03)
        if vida == 100:
            print(f'            {"_"*10}')
            print('vida:100%  |##########|')
            print(f'ARMA:espada {"-" * 10}')
    #atualiza a tela quando não é o inicio
    else:
        print(f'-{direcao[dir]: >9}{"-": >9}')
        if not vida_inimigo == 0 and sit == False:
            if dir == 2 and vida_inimigo > 0:
                l = 3
                if 1 in tela[l]:
                    for j in range(0,4):
                        if j > 1:
                            for i in range(0,2):
                                tela[j][l] = 8
                                tela[j][l+1] = 8
                sit = True
        elif vida_inimigo == 0:
            for cx in tela:
                if 1 in cx and 8 in cx:
                    pos1 = cx.index(8)
                    cx[pos1] = 1
                    cx[pos1+1] = 1
                if 0 in cx and 8 in cx:
                    pos1 = cx.index(8)
                    cx[pos1] = 0
                    cx[pos1+1] = 0
        for linha in tela:
            for l in linha:
                print(l,end=' ')
            print()
            time.sleep(0.03)
        if sit == True:
            vida -= 25
        if vida == 100:
            print(f'            {"_"*10}')
            print('vida:100%  |##########|')
            print(f'ARMA:espada {"-" * 10}')
        if vida == 75:
            print(f'            {"_" * 10}')
            print('vida:75%   |########  |')
            print(f'ARMA:espada {"-" * 10}')
        if vida == 50:
            print(f'            {"_" * 10}')
            print('vida:50%   |#####     |')
            print(f'ARMA:espada {"-" * 10}')
        if vida == 25:
            print(f'            {"_" * 10}')
            print('vida:25%   |###       |')
            print(f'ARMA:espada {"-" * 10}')
        if vida == 0:
            print(f'            {"_" * 10}')
            print('vida:0%    |          |')
            print(f'ARMA:espada {"-" * 10}')
            time.sleep(4)
            os.system('cls')
            for l in tela:
                del (l[:])
                for c in range(0, 10):
                    l.append(0)
            del (tela[3][:])
            palavra = '-=-=você morreu=-=- '
            tela[3].append(palavra)
            for linha in tela:
                for li in linha:
                    print(li,end=' ')
                print()
            break
        if ata:
            l = 2
            l2 = 6
            for c in range(0,4):
                tela[l][l2] = 3
                l += 1
                l2 += 1
            print('vuuuuuusshhh')
            time.sleep(0.6)
            os.system('cls')
            for l in tela:
                for lm in l:
                    print(lm, end=' ')
                print()
                time.sleep(0.03)
            if vida == 100:
                print(f'            {"_" * 10}')
                print('vida:100%  |##########|')
                print(f'ARMA:espada {"-" * 10}')
            if vida == 75:
                print(f'            {"_" * 10}')
                print('vida:75%  |########  |')
                print(f'ARMA:espada {"-" * 10}')
            if vida == 50:
                print(f'            {"_" * 10}')
                print('vida:50%  |#####     |')
                print(f'ARMA:espada {"-" * 10}')
            if vida == 25:
                print(f'            {"_" * 10}')
                print('vida:25%  |###       |')
                print(f'ARMA:espada {"-" * 10}')
            if vida == 0:
                print(f'            {"_" * 10}')
                print('vida:0%  |          |')
                print(f'ARMA:espada {"-" * 10}')
                time.sleep(4)
                os.system('cls')
                for l in tela:
                    del (l[:])
                    for c in range(0, 10):
                        l.append(0)
                del (tela[3][:])
                palavra = '-=-=você morreu=-=- '
                tela[3].append(palavra)
                for cx in tela:
                    for ch in cx:
                        print(ch,end=' ')
                    print()
                break
        ata = False
    #le o comando dado pelo jogador
    mov = input('movimento/ação: ')
    #termina o jogo
    if mov == 'end':
        break
    #back-end\ comunica para o ''front-end atualizar'' a espada
    if mov == 'atacar':
        l = 2
        l2 = 6
        for c in range(0,4):
            if not 0 in tela[l]:
                tela[l][l2] = 1
            else:
                tela[l][l2] = 0
            l += 1
            l2 += 1
        ata = True
        if sit == True:
            vida_inimigo -= 25
        if vida_inimigo == 0:
            sit = False
    #comunica ao ''front-end'' para atualizar o chão
    if mov == 'w' and sit == False:
        achou = False
        for linha in tela:
            if 1 in linha:
                achou = True
                pos = 0
                achou2 = False
                if 3 in linha:
                    pos = linha.index(3)
                    achou2 = True
                del (linha[:])
                for ci in range(0, 10):
                    linha.append(0)
                if achou2 == True:
                    linha[pos] = 3
                break
        if achou == False:
            os.system('cls')
            print('caiu no vazio')
            for l in tela:
                del (l[:])
                for ck in range(0, 10):
                    l.append(0)
            for l in tela:
                for lm in l:
                    print(lm, end=' ')
                print()
                time.sleep(0.03)
            break
    # comunica os ''front-end'' para atualizar a direcao
    elif mov in ['a','d','s'] and sit == False:
        if mov == 'a':
            if dir == 0:
                dir = 3
            else:
                dir -= 1
        elif mov == 'd':
            if dir == 3:
                dir = 0
            else:
                dir += 1
        elif mov == 's':
            achou = False
            for l in tela[::-1]:
                if not 1 in l:
                    achou2 = False
                    achou = True
                    if 3 in l:
                        pos = l.index(3)
                        achou2 = True
                    del (l[:])
                    for ck in range(0, 10):
                        l.append(1)
                    if achou2 == True:
                        l[pos] = 3
                    break
            if achou == False:
                os.system('cls')
                print('caiu no vazio')
                for l in tela:
                    del (l[:])
                    for ck in range(0, 10):
                        l.append(0)
                for l in tela:
                    for lm in l:
                        print(lm, end=' ')
                    print()
                    time.sleep(0.03)
                break

    else:
        print('movimento invalido')
    os.system('cls')
    c += 1
