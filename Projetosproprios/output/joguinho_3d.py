import os
import random
import time
import threading
import datetime

def som():
    import winsound
    while True:
        winsound.PlaySound("musicaventura.wav", winsound.SND_FILENAME)

thread = threading.Thread(target=som,args=())
thread.start()
# há 12 dias construindo
# debug de posição de criação de objetos
def linha(btf=False):
    if btf == False:
        print('-'*30)
    elif btf == True:
        print('-='*15)
def derrota():
    print('\033[33m',end='')
    linha(True)
    print('\033[33m',end='')
    print('\033[31m',end='')
    linha()
    print(f'=-    Morto em 1616/{datetime.datetime.now().month}/{datetime.datetime.now().day}    -=')
    linha()
    print('\033[m',end='')
    print('\033[33m', end='')
    linha(True)
    print('\033[33m', end='')
    input()
def frames_combate(acao):
    if acao == 1:
        print('\033[33m_ _ _ _\n|     |\n|  =  |\n\     /\n \ _ /\033[m')
    elif acao == 2:
        print('\033[31m   |       \n   |        \n   |   \n|=====|\n   #      \033[m')
    elif acao == 3:
        print('\033[32m     _______\n    /       \ \n __ | \ _ / |__\n \_ | * _ * |_ /\n    \ ===== /\n      -----\033[m')
def combate():
    global sit_vida
    os.system('cls')
    datamy = {'vida':100,'atan':20,'atas':25}
    datamont = {'vida':100,'atan':20,'atas':35}
    vez = True
    defe = False
    while True:
        if datamy['vida'] <= 0:
            print('\033[31mvocê morreu!\033[m')
            sit_vida = False
            break
        elif datamont['vida'] <= 0:
            print('\033[33mvocê matou o monstro!\033[m')
            break
        if vez == True:
            print('\033[35m-=\033[m' * 15)
            print('\033[33m-=     SEUS DADOS DE BATALHA     =-\033[m')
            print(f'vida:{datamy['vida']},ataque normal:{datamy['atan']},ataque super:{datamy['atas']}')
            acao = input('ação (\033[31matacar\033[m ou \033[34mdefender\033[m): ')
            if acao.strip() == 'atacar':
                frames_combate(2)
                datamont['vida'] -= random.choice([datamy['atan'],datamy['atas']])
            elif acao.strip() == 'defender':
                frames_combate(1)
                defe = True
            vez = False
            print('\033[35m-=\033[m' * 15)
        else:
            print('\033[33m-=     DADOS DO MONSTRO     =-\033[m')
            acao = random.choice(['atacar','nada'])
            print(f'vida:{datamont['vida']},ataque normal:{datamont['atan']},ataque super:{datamont['atas']}')
            frames_combate(3)
            print(f'ação:{acao}')
            if acao == 'atacar' and defe == False:
                datamy['vida'] -= random.choice([datamont['atan'],datamont['atas']])
            elif defe == True:
                defe = False
            vez = True
        time.sleep(6)
        os.system('cls')
def elimina_regs_mont(y,x):
    global monts
    for pos, mont in enumerate(monts):
        if mont[0] == y and mont[1] == x:
            del monts[pos]
def trata_mont(y,x,posv,dist):
    global sit_vida
    global mapa
    if dist < 2:
        print(f'monstro encontrado pos({y} {x})')
        combate()
        if sit_vida == True:
            elimina_regs_mont(y,x)
            mapa[y][x] = ' '
    atualiza_tela(dist,posv,True)
def mostra_mapa():
    global mapa
    global pos_objs
    global pos_x
    global pos_y
    global monts
    global tela_visual
    for mont in monts:
        mapa[mont[0]][mont[1]] = '@'
    for pos in pos_objs:
        mapa[pos[0]][pos[1]] = '/'
    mapa[pos_y][pos_x] = '&'
    for linha in mapa:
        for coluna in linha:
            print(coluna,end=' ')
        print()
#atualizações de interface
def atualiza_tela(dist,quant,show=False):
    if show == False:
        if dist < 0:
            dist = 0
        if abs(dist) == 0:
            for linha in tela_visual:
                linha[quant] = '\033[34m#\033[m'
        elif abs(dist) == 1:
            for linha2 in tela_visual[1:]:
                linha2[quant] = '\033[34m#\033[m'
        elif abs(dist) == 2:
            for linha3 in tela_visual[2:]:
                linha3[quant] = '\033[34m#\033[m'
        else:
            for linha4 in tela_visual[3:]:
                linha4[quant] = '\033[34m#\033[m'
    else:
        if dist < 0:
            dist = 0
        if abs(dist) == 0:
            for linha in tela_visual[1:]:
                linha[quant] = '\033[32m%\033[m'
        elif abs(dist) == 1:
            for linha2 in tela_visual[1:]:
                linha2[quant] = '\033[32m%\033[m'
        elif abs(dist) == 2:
            for linha3 in tela_visual[2:]:
                linha3[quant] = '\033[32m%\033[m'
        else:
            for linha4 in tela_visual[3:]:
                linha4[quant] = '\033[32m%\033[m'
#raycasting
def raysting():
    global rotacao
    global pos_x
    global pos_y
    global mapa
    if rotacao == 0:
        for pos, obj in enumerate(mapa[pos_y-1][:pos_x]):
            if pos <= pos_x:
                if obj == '/':
                    dist2 = (pos_x - pos) - 1
                    atualiza_tela(dist2,4)
                elif obj == '@':
                    dist2 = (pos_x - pos) - 1
                    trata_mont(pos_y-1,pos,4,dist2)
        for pos2, obj3 in enumerate(mapa[pos_y][:pos_x]):
            if pos2 <= pos_x:
                if obj3 == '/':
                    dist = (pos_x-pos2)-1
                    atualiza_tela(dist,3)
                elif obj3 == '@':
                    dist = (pos_x - pos2) - 1
                    trata_mont(pos_y,pos2,3,dist)
        for pos3, obj4 in enumerate(mapa[pos_y+1][:pos_x]):
            if pos3 <= pos_x:
                if obj4 == '/':
                    dist = (pos_x - pos3) - 1
                    atualiza_tela(dist,2)
                elif obj4 == '@':
                    dist = (pos_x - pos3) - 1
                    trata_mont(pos_y + 1, pos3,2,dist)
    elif rotacao == 90:
        for pos, obj in enumerate(mapa):
            if pos <= pos_y:
                if mapa[pos][pos_x] == '/':
                    dist = (pos_y - pos) - 1
                    atualiza_tela(dist,4)
                elif mapa[pos][pos_x] == '@':
                    dist = (pos_x - pos) - 1
                    trata_mont(pos, pos_x,4,dist)
            for pos2, obj3 in enumerate(mapa):
                if pos2 <= pos_y:
                    if mapa[pos2][pos_x-1] == '/':
                        dist = (pos_y - pos2) - 1
                        atualiza_tela(dist,3)
                    elif mapa[pos2][pos_x-1] == '@':
                        dist = (pos_x - pos2) - 1
                        trata_mont(pos2, pos_x-1, 3, dist)
            for pos3, obj3 in enumerate(mapa):
                if pos3 <= pos_y:
                    if mapa[pos3][pos_x+1] == '/':
                        dist = (pos_y - pos3) - 1
                        atualiza_tela(dist,5)
                    elif mapa[pos3][pos_x+1] == '@':
                        dist = (pos_x - pos3) - 1
                        trata_mont(pos3, pos_x+1, 5, dist)
    elif 0 < rotacao < 90:
        cont = 0
        for pos, obj in enumerate(mapa):
            if cont <= 6:
                if (0+cont) < pos_x:
                    if mapa[pos][(0+cont)] == '/':
                        dist = ((pos_x-1)-pos)
                        atualiza_tela(dist,3)
                    elif mapa[pos][(0+cont)] == '@':
                        dist = ((pos_x-1)-pos)
                        trata_mont(pos,(0+cont),3,dist)
                cont += 1
            else:
                break
        cont2 = 0
        for pos2, obj2 in enumerate(mapa):
            if pos2 <= 6:
                if (1 + cont2) < pos_x:
                    if mapa[pos2][(1 + cont2)] == '/':
                        dist = ((pos_x - 1) - pos2) - 1
                        atualiza_tela(dist,4)
                    elif mapa[pos2][(1+cont2)] == '@':
                        dist = ((pos_x-1)-pos2)-1
                        trata_mont(pos2,(1+cont2),4,dist)
            cont2 += 1
        cont3 = 0
        for pos3, obj3 in enumerate(mapa):
            if pos3 < pos_y:
                if (cont3-1) >= 0 and (cont3 -1) < pos_x:
                    dist = cont3-1
                    atualiza_tela(dist,2)
                elif mapa[pos3][(1 + cont3)] == '@':
                    dist = ((pos_x - 1) - pos3) - 1
                    trata_mont(pos3, (1 + cont3), 4, dist)
            cont3 += 1
    elif rotacao == 180:
        for pos, obj in enumerate(mapa):
            if pos == pos_y:
                for posm, objm in enumerate(obj):
                    if posm > pos_x and objm == '/':
                        dist = (posm-pos_x)-1
                        atualiza_tela(dist,3)
                        break
                    elif posm > pos_x and objm == '@':
                        dist = (posm-pos_x)-1
                        trata_mont(pos,posm,3,dist)
                        break
        for pos, obj in enumerate(mapa):
            if pos == pos_y-1:
                for posm, objm in enumerate(obj):
                    if posm > pos_x and objm == '/':
                        dist = (posm-pos_x)-1
                        atualiza_tela(dist,2)
                        break
                    elif posm > pos_x and objm =='@':
                        dist = (posm-pos_x)-1
                        trata_mont(pos,posm,2,dist)
                        break
        for pos, obj in enumerate(mapa):
            if pos == pos_y+1:
                for posm, objm in enumerate(obj):
                    if posm > pos_x and objm == '/':
                        dist = (posm-pos_x)-1
                        atualiza_tela(dist,4)
                        break
                    if posm > pos_x and objm == '@':
                        dist = (posm-pos_x)-1
                        trata_mont(pos,posm,4,dist)
                        break
    elif 90 < rotacao and rotacao < 180:
        cont = 0
        for pos, obj in enumerate(mapa):
            if pos <= 6-(6-pos_y):
                dado = 6-(6-pos_y)
                for posm, objm in enumerate(obj):
                    if posm > pos_x and objm == '/':
                        vezes = dado
                        for c in range(0,vezes):
                            if not dado < 6:
                                break
                            else:
                                dado += 1
                        dado-=cont
                        if dado == posm:
                            dist = vezes-1
                            atualiza_tela(dist+1,3)
                        dado = vezes
                    if posm > pos_x and objm == '@':
                        vezes = dado
                        for c in range(0, vezes):
                            if not dado < 6:
                                break
                            else:
                                dado += 1
                        dado -= cont
                        if dado == posm:
                            dist = vezes - 1
                            trata_mont(pos,posm,3,dist)
            cont+= 1
        cont = 0
        for pos2, obj2, in enumerate(mapa):
            if pos2 <= 6 - (6 - pos_y):
                dado = 6 - (6 - pos_y)
                for posm, objm in enumerate(obj2):
                    if posm > pos_x and objm == '/':
                        vezes = dado
                        for c in range(0, vezes):
                            if not dado < 6:
                                break
                            else:
                                dado += 1
                        dado -= (cont+1)
                        if dado == posm:
                            dist = vezes
                            atualiza_tela(dist,4)
                        dado = vezes
                    if posm > pos_x and objm == '@':
                        vezes = dado
                        for c in range(0, vezes):
                            if not dado < 6:
                                break
                            else:
                                dado += 1
                        dado -= (cont + 1)
                        if dado == posm:
                            dist = vezes - 1
                            trata_mont(pos2, posm, 4, dist)
        cont += 1
        cont = 0
        for pos, obj in enumerate(mapa):
            if pos <= 6 - (6 - pos_y):
                dado = 6 - (6 - pos_y)
                for posm, objm in enumerate(obj):
                    if posm > pos_x and objm == '/':
                        vezes = dado
                        for c in range(0, vezes):
                            if not dado < 6:
                                break
                            else:
                                dado += 1
                        dado -= (cont-1)
                        if dado == posm:
                            dist = vezes - 1
                            atualiza_tela(dist,2)
                        dado = vezes
                    if posm > pos_x and objm == '@':
                        vezes = dado
                        for c in range(0, vezes):
                            if not dado < 6:
                                break
                            else:
                                dado += 1
                        dado -= (cont - 1)
                        if dado == posm:
                            dist = vezes - 1
                            trata_mont(pos,posm,2,dist)
            cont += 1
    elif rotacao == 270:
        cont = 0
        for pos, obj in enumerate(mapa):
            if pos >= pos_y:
                if obj[pos_x] == '/':
                    atualiza_tela(cont-1,3)
                    break
                if obj[pos_x] == '@':
                    trata_mont(pos,pos_x,3,cont-1)
                    break
                cont += 1
        cont = 0
        for pos, obj in enumerate(mapa):
            if pos >= pos_y:
                if obj[pos_x-1] == '/':
                    atualiza_tela(cont-1, 2)
                    break
                if obj[pos_x-1] == '@':
                    trata_mont(pos,pos_x-1,2,cont-1)
                    break
                cont += 1
        cont = 0
        for pos, obj in enumerate(mapa):
            if pos >= pos_y:
                if obj[pos_x+1] == '/':
                    atualiza_tela(cont- 1, 4)
                    break
                if obj[pos_x+1] == '@':
                    trata_mont(pos,pos_x+1,4,cont-1)
                    break
                cont += 1
def raycasting2():
    global rotacao
    global pos_x
    global pos_y
    global mapa
    if 180 < rotacao and rotacao < 270:
        cont = 6-pos_y
        dist = 0
        for cont2 in range(0,cont+1):
            if pos_y+cont2 < 6 and pos_x < 5:
                if mapa[pos_y+cont2][pos_x+cont2] == '/':
                    atualiza_tela(dist-1,3)
                    break
                elif mapa[pos_y+cont2][pos_x+cont2] == '@':
                    trata_mont((pos_y+cont2),(pos_x+cont2),3,dist - 1)
                    break
                else:
                    dist += 1
            else:
                break
        dist = 0
        for cont3 in range(0,cont+1):
            if (pos_y+cont3)+1 < 6 and pos_x < 5:
                if mapa[(pos_y+cont3)+1][(pos_x+cont3)] == '/':
                    atualiza_tela(dist-1,4)
                    break
                elif mapa[(pos_y+cont3)+1][pos_x+cont3] == '@':
                    trata_mont(((pos_y+cont3)+1),(pos_x+cont3),4,dist - 1)
                    break
                else:
                    dist += 1
            else:
                break
        dist = 0
        for cont3 in range(0, cont+1):
            if (pos_y + cont3) - 1 < 6 and pos_x < 5:
                if mapa[(pos_y + cont3) - 1][(pos_x + cont3)] == '/':
                    atualiza_tela(dist - 1, 2)
                    break
                elif mapa[pos_y+cont3][pos_x+cont3-1] == '@':
                    trata_mont((pos_y+cont3)-1,(pos_x+cont3),2,dist - 1)
                    break
                else:
                    dist += 1
            else:
                break
    elif 360 > rotacao and rotacao > 270:
        cont = 6-pos_y
        dist = 0
        for c in range(0,cont):
            if pos_y+c < 6 and pos_x > 0:
                if mapa[pos_y+c][pos_x-c] == '/':
                    atualiza_tela(dist-1,3)
                    break
                elif mapa[pos_y+c][pos_x-c] == '@':
                    trata_mont((pos_y+c),(pos_x-c),3,dist-1)
                    break
                else:
                    dist += 1
            else:
                break
        dist = 0
        for c in range(0, cont):
            if pos_y + c+1 < 6 and pos_x > 0:
                if mapa[pos_y + c+1][pos_x - c] == '/':
                    atualiza_tela(dist - 1, 2)
                    mapa[pos_y + c + 1][pos_x - c] = '.'
                    break
                elif mapa[(pos_y+c)+1][pos_x-c] == '@':
                    trata_mont((pos_y+c)+1,(pos_x-c),2,dist-1)
                    break
                else:
                    dist += 1
            else:
                break
        dist = 0
        for c in range(0, cont):
            if pos_y + c-1 < 6 and pos_x > 0:
                if mapa[pos_y + c-1][pos_x - c] == '/':
                    atualiza_tela(dist - 1, 4)
                    mapa[pos_y + c-1][pos_x - c] = '.'
                    break
                elif mapa[pos_y+c][pos_x-c] == '@':
                    trata_mont((pos_y+c)-1,(pos_x-c),4,dist-1)
                    break
                else:
                    dist += 1
            else:
                break
    for linha2 in tela_visual:
        for pos, coluna in enumerate(linha2):
            print(coluna, end=' ')
            linha2[pos] = ' '
        print()
# movimento
def w_acao():
    global mapa
    global pos_x
    global pos_y
    global rotacao
    mapa[pos_y][pos_x] = ' '
    if rotacao == 0:
        if pos_x > 0 and mapa[pos_y][pos_x - 1] != '/' and mapa[pos_y][pos_x-1] != '@':
            pos_x -= 1
    elif rotacao == 90:
        if pos_y > 0 and mapa[pos_y-1][pos_x] != '/' and mapa[pos_y-1][pos_x] != '@':
            pos_y -= 1
    elif rotacao == 180 and pos_x < 5:
        if pos_x < 5 and mapa[pos_y][pos_x + 1] != '/' and mapa[pos_y][pos_x + 1] != '@':
            pos_x += 1
    elif rotacao == 270 and pos_y < 6:
        if pos_y > 0 and mapa[pos_y+1][pos_x] != '/' and mapa[pos_y+1][pos_x] != '@':
            pos_y += 1
    elif rotacao > 0 and rotacao < 90:
        if pos_y > 0 and pos_x > 0 and mapa[pos_y-1][pos_x-1] != '/' and mapa[pos_y-1][pos_x-1] != '@':
            pos_y -= 1
            pos_x -= 1
    elif rotacao > 90 and rotacao < 180:
        if pos_y > 0 and pos_x < 6 and mapa[pos_y-1][pos_x+1] != '/' and mapa[pos_y-1][pos_x+1] != '@':
            pos_y -= 1
            pos_x += 1
    elif rotacao > 180 and rotacao < 270:
        if pos_y < 6 and pos_x < 6 and mapa[pos_y+1][pos_x+1] != '/' and mapa[pos_y+1][pos_x+1] != '@':
            pos_y += 1
            pos_x += 1
    elif rotacao > 270 and rotacao < 360:
        if pos_y < 6 and pos_x > 0 and mapa[pos_y+1][pos_x-1] != '/' and mapa[pos_y+1][pos_x-1] != '@':
            pos_y += 1
            pos_x -= 1
            
tela_visual = [[' ',' ',' ',' ',' ',' ',' '],
               [' ',' ',' ',' ',' ',' ',' '],
               [' ',' ',' ',' ',' ',' ',' '],
               [' ',' ',' ',' ',' ',' ',' '],
               [' ',' ',' ',' ',' ',' ',' '],
               [' ',' ',' ',' ',' ',' ',' '],
               [' ',' ',' ',' ',' ',' ',' ']]

mapa = [[' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ']]

monts = [[3,1]]
pos_objs = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(1,0),(1,5),(2,0),(2,5),(3,0),(3,5),(4,0),(4,5),(5,0),(5,5),(6,0),(6,1),
            (6,2),(6,3),(6,4),(6,5),(4,1),(4,3)]

sit_vida = True
pos_x = 2
pos_y = 1
rotacao = 0

while True:
    if sit_vida == False:
        os.system('cls')
        derrota()
        break
    print('-'*11)
    mostra_mapa()
    print('-' * 11)
    raysting()
    raycasting2()
    print(rotacao)
    acao = input('Escolha a ação que deseja fazer (W,S,D): ')
    if acao == 'a':
        if rotacao == 0:
            rotacao = 360 - 30
        else:
            rotacao -= 30
    if acao == 'd':
        if rotacao == 360:
            rotacao = 0
        else:
            rotacao += 30
    elif acao == 'w':
        w_acao()
    os.system('cls')