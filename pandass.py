import time
import random
def m1():
    print("-=    Calculadora de x    =-")
    valor_igual = int(input('Qual valor será igual a multiplicação: '))
    print(f"{valor_igual} = ? . ?")
    valor_descoberto = int(input('Qual o primeiro fator o que se sabe o valor: '))
    print(f"{valor_igual} = {valor_descoberto} . x")
    print(f"=-   Calculando o valor de x ",end=' ')
    for c in range(0,3):
        time.sleep(1)
        print('.', end=' ')
    print('   -=')
    if valor_descoberto < valor_igual:
        print(f"   O valor de x é {valor_igual / valor_descoberto}")
    else:
        print(f"   O valor de x é {valor_descoberto / valor_igual}")
def m2():
    x = 4
    print("-=    Calculadora de dano    =-")
    for c in range(0, 20):
        valor_igual = random.randint(1,20)
        valor_descoberto = random.randint(1, 20)
        print(f"A força foi {valor_descoberto}, o dano foi {valor_descoberto*x}")
'''import os
import time


def atualiza_tela():
    global tela
    global z
    chao = 6 - z
    print(chao)
    for pos, linha2 in enumerate(tela):
        if pos >= chao and z <= 3:
            tela[pos] = ['#', '#', '#', '#', '#', '#', '#']


def desenha_tela():
    global tela
    global z
    for linha in tela:
        for coluna in linha:
            if coluna == ' ':
                print(f'\033[0;0;44m{coluna}\033[m', end='\033[0;0;44m \033[m')
            elif coluna == '#':
                print(f'\033[32;0;42m{coluna}\033[m', end='\033[32;0;42m \033[m')
        print()
    for pos3, linha3 in enumerate(tela):
        tela[pos3] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
    if z > 3:
        for pos, linha2 in enumerate(tela):
            if pos >= 3 and z > 3:
                tela[pos] = ['#', '#', '#', '#', '#', '#', '#']


def linha():
    print('-' * 30)


tela = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
z = 1
while True:
    atualiza_tela()
    linha()
    desenha_tela()
    linha()
    print(f'O eixo z e igual a: {z}')
    acao = input('Deseja fazer o que: subir(w), descer(s); ').strip()
    if z == 1 and acao == 's':
        print('\033[31mVocê já se encontra no chão\033[m')
    elif z > 1 and acao == 's':
        z -= 1
    elif acao == 'w':
        z += 1
    time.sleep(2)
    os.system('cls)'''