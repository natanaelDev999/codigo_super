import os

def mostra_mapa():
    global mapa
    global pos_objs
    global pos_x
    global pos_y
    for pos in pos_objs:
        mapa[pos[0]][pos[1]] = '/'
    mapa[pos_y][pos_x] = '&'
    for linha in mapa:
        for coluna in linha:
            print(coluna,end=' ')
        print()
def atualiza_tela(dist,quant):
    if dist == 0:
        for linha in tela_visual:
            linha[quant] = '#'
    elif dist == 1:
        for linha2 in tela_visual[1:]:
            linha2[quant] = '#'
    elif dist == 2:
        for linha3 in tela_visual[2:]:
            linha3[quant] = '#'
    elif dist == 3:
        for linha4 in tela_visual[3:]:
            linha4[quant] = '#'
def raysting():
    global rotacao
    global pos_x
    global pos_y
    global mapa
    if rotacao == 0:
        for pos, obj in enumerate(mapa[pos_y-1][:pos_x]):
            print(obj)
            if pos <= pos_x:
                if obj == '/':
                    dist2 = (pos_x - pos) - 1
                    print(f'x:{pos};y:{pos_y};obj:{obj};linha:{mapa[pos_y -1]};dist:{dist2}')
                    atualiza_tela(dist2,4)
        for pos2, obj3 in enumerate(mapa[pos_y][:pos_x]):
            print(obj3)
            if pos2 <= pos_x:
                if obj3 == '/':
                    dist = (pos_x-pos2)-1
                    print(f'x:{pos2};y:{pos_y};obj:{obj3};linha:{mapa[pos_y]};dist:{dist}')
                    atualiza_tela(dist,3)
        for pos3, obj4 in enumerate(mapa[pos_y+1][:pos_x]):
            print(obj4)
            if pos3 <= pos_x:
                if obj4 == '/':
                    dist = (pos_x - pos3) - 1
                    print(f'x:{pos3};y:{pos_y};obj:{obj4};linha:{mapa[pos_y+1]};dist:{dist}')
                    atualiza_tela(dist,2)
    elif rotacao == 90:
        for pos, obj in enumerate(mapa):
            if pos <= pos_y:
                if mapa[pos][pos_x] == '/':
                    dist = (pos_y - pos) - 1
                    print(f'dist: {dist};obj{mapa[pos][pos_x]};pos:{pos}\033[31m/\033[m',end=' ')
                    atualiza_tela(dist,4)
            for pos2, obj3 in enumerate(mapa):
                if pos2 <= pos_y:
                    if mapa[pos2][pos_x-1] == '/':
                        dist = (pos_y - pos2) - 1
                        print(f'dist: {dist};obj{mapa[pos2][pos_x-1]};pos:{pos2}\033[31m/\033[m',end=' ')
                        atualiza_tela(dist,3)
            for pos3, obj3 in enumerate(mapa):
                if pos3 <= pos_y:
                    if mapa[pos3][pos_x+1] == '/':
                        dist = (pos_y - pos3) - 1
                        print(f'dist: {dist};obj{mapa[pos3][pos_x+1]};pos:{pos3}\033[31m/\033[m',end=' ')
                        atualiza_tela(dist,5)
            print()
    elif 0 < rotacao < 90:
        cont = 0
        for pos, obj in enumerate(mapa):
            if cont <= 6:
                if (0+cont) < pos_x:
                    print((0+cont))
                    print(f'pos:{pos};obj:{obj};obj pos:{mapa[pos][(0+cont)]}')
                    if mapa[pos][(0+cont)] == '/':
                        dist = ((pos_x-1)-pos)
                        print(f'/ foi encontrado,distância:{dist}')
                        atualiza_tela(dist,3)
                cont += 1
            else:
                break
        cont2 = 0
        for pos2, obj2 in enumerate(mapa):
            if pos2 <= 6:
                if (1 + cont2) < pos_x:
                    print(f'obj:{mapa[pos2][(1 + cont2)]};pos y:{pos2};pos x:{(1 + cont2)};obj tot:{mapa[pos2]}')
                    if mapa[pos2][(1 + cont2)] == '/':
                        dist = ((pos_x - 1) - pos2) - 1
                        print(f'{mapa[pos2][(1 + cont2)]},pos:({pos2},{(1 + cont2)}),dist:{dist}')
                        atualiza_tela(dist,4)
            cont2 += 1
        cont3 = 0
        for pos3, obj3 in enumerate(mapa):
            if pos3 < pos_y:
                if (cont3-1) >= 0 and (cont3 -1) < pos_x:
                    dist = cont3-1
                    print(f'pos:{pos3},obj:{mapa[pos3][(cont3-1)]},dist:{dist}')
                    atualiza_tela(dist,2)
            cont3 += 1
    elif rotacao == 180:
        for pos, obj in enumerate(mapa):
            if pos == pos_y:
                for posm, objm in enumerate(obj):
                    if posm > pos_x and objm == '/':
                        dist = (posm-pos_x)-1
                        print(f'obj:{objm},pos:{posm},dist:{dist}',end=' ')
                        print()
                        atualiza_tela(dist,3)
                        break
        for pos, obj in enumerate(mapa):
            if pos == pos_y-1:
                for posm, objm in enumerate(obj):
                    if posm > pos_x and objm == '/':
                        dist = (posm-pos_x)-1
                        print(f'obj:{objm},pos:{posm},dist:{dist}',end=' ')
                        print()
                        atualiza_tela(dist,2)
                        break
        for pos, obj in enumerate(mapa):
            if pos == pos_y+1:
                for posm, objm in enumerate(obj):
                    if posm > pos_x and objm == '/':
                        dist = (posm-pos_x)-1
                        print(f'obj:{objm},pos:{posm},dist:{dist}',end=' ')
                        print()
                        atualiza_tela(dist,4)
                        break
    elif 90 < rotacao and rotacao < 180:
        cont = 0
        for pos, obj in enumerate(mapa):
            if pos < 6-(6-pos_y):
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
                            print(f'pos y:{pos};pos x:{posm};obj:{objm},dist player:{dist}', end=';validação:')
                            print('posição válida')
                            atualiza_tela(dist,3)
                        dado = vezes
            cont+= 1
        cont = 0
        for pos2, obj2, in enumerate(mapa):
            if pos2 < 6 - (6 - pos_y):
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
                            print(f'pos y:{pos2};pos x:{posm};obj:{objm},dist player:{dist}', end=';validação:')
                            print('posição válida')
                            atualiza_tela(dist,4)
                        dado = vezes
        cont += 1
        cont = 0
        for pos, obj in enumerate(mapa):
            if pos < 6 - (6 - pos_y):
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
                            print(f'pos y:{pos};pos x:{posm};obj:{objm},dist player:{dist}', end=';validação:')
                            print('posição válida')
                            atualiza_tela(dist,2)
                        dado = vezes
            cont += 1
    for linha2 in tela_visual:
        for pos, coluna in enumerate(linha2):
            print(coluna, end=' ')
            linha2[pos] = ' '
        print()

def w_acao():
    global mapa
    global pos_x
    global pos_y
    global rotacao
    mapa[pos_y][pos_x] = ' '
    if rotacao == 0:
        if pos_x > 0 and mapa[pos_y][pos_x - 1] != '/':
            pos_x -= 1
    elif rotacao == 90:
        if pos_y > 0 and mapa[pos_y-1][pos_x] != '/':
            pos_y -= 1
    elif rotacao == 180 and pos_x < 5:
        if pos_x < 5 and mapa[pos_y][pos_x + 1] != '/':
            pos_x += 1
    elif rotacao == 270 and pos_y < 6:
        if pos_y > 0 and mapa[pos_y+1][pos_x] != '/':
            pos_y += 1

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

pos_objs = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(1,0),(1,5),(2,0),(2,5),(3,0),(3,5),(4,0),(4,5),(5,0),(5,5),(6,0),(6,1),
            (6,2),(6,3),(6,4),(6,5)]

pos_x = 2
pos_y = 2
rotacao = 0

while True:
    print('-'*11)
    mostra_mapa()
    print('-' * 11)
    raysting()
    print(rotacao)
    acao = input('Escolha a ação que deseja fazer: ')
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