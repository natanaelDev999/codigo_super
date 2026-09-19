###############################################################
#                     LibraryRenderNatanT
###############################################################
# criação do projeto: 18/09/2026
# termino do projeto:
# intervalo de tempo:
###############################################################
#                 bibliotecas utilizadas
# biblioteca para manipulação do terminal
import sys
# biblioteca para manipulação de fps
import time
# biblioteca para matemática
import math
# biblioteca para trabalhar com vetores
import LibraryVectorNatan as lvn
###############################################################
#                         buffers
# Buffer de Dados para Vértices(BDV)
bdv = []
# Buffer de Dados para Aparência(BDA)
bda = []
###############################################################
#                          tela
tela = []
largura = 0
altura = 0
###############################################################
#                     FUNÇÕES UTILITÁRIAS
# função para adicionar dados aos bufffers
def adiciona_dados(tipo,dados):
    global bdv,bda
    if len(dados) > 0:
        if tipo == "BDV" or tipo == "Buffer de Dados para Vértices":
            bdv = dados
        elif tipo == "BDA" or tipo == "Buffer de Dados para Aparência":
            bda = dados
# projeta vértices
def projeta_vertices():
    global bdv,largura,altura,bda
    proj = []
    for pos0,p in enumerate(bdv):
        if p[2] > 0:
            proj.append([int((p[0]/p[2])+(largura/2)),
                         int((p[1]/p[2])+(altura/2)),pos0])
            if (p[0] / p[2]) + (largura / 2) < largura and (p[1] / p[2]) + (altura / 2) < altura:
                if pos0 < len(bda):
                    tela[int((p[1]/p[2])+(altura/2))][int((p[0]/p[2])+(largura/2))] = f'\033[38;2;{bda[pos0][0]};{bda[pos0][1]};{bda[pos0][2]}m█\033[m'
    return proj
# cria linha
def desenha_linhas(proj):
    global tela,largura,altura,bda
    ponto1 = []
    ponto2 = []
    # obtenção dos vértices
    for pos0, c in enumerate(proj):
        if pos0 % 2 == 0:
            ponto1.append(c)
        elif pos0 % 2 != 0:
            ponto2.append(c)
    # cálculos para desenho de linha
    for pos1,v in enumerate(ponto1):
        if pos1 < len(ponto2):
            dx = abs(ponto2[pos1][0] - v[0])
            dy = abs(ponto2[pos1][1] - v[1])
            passo_x = 0
            if v[0] < ponto2[pos1][0]:
                passo_x = 1
            else:
                passo_x = -1

            passo_y = 0
            if v[1] < ponto2[pos1][1]:
                passo_y = 1
            else:
                passo_y = -1

            cor1 = bda[v[2]]
            cor2 = bda[ponto2[pos1][2]]

            x = v[0]
            y = v[1]

            if dx > dy:
                p = 2 * dy - dx
                while abs(int(x)) != int(abs(ponto2[pos1][0])):
                    if y < altura and x < largura:
                        corf = lvn.divide_vetores(lvn.soma_vetores(cor1, cor2), [x, y, 2])
                        tela[y][x] = f'\033[38;2;{int(corf[0])};{int(corf[1])};{int(corf[2])}m█\033[m'
                    if p >= 0:
                        y += passo_y
                        p += 2 * (dy - dx)
                    else:
                        p += 2 * dy
                    x += passo_x
            else:
                p = 2 * dx - dy
                while abs(int(y)) != abs(int(ponto2[pos1][1])):
                    if y < altura and x < largura:
                        corf = lvn.divide_vetores(lvn.soma_vetores(cor1,cor2),[x,y,1])
                        tela[y][x] =  f'\033[38;2;{int(corf[0])};{int(corf[1])};{int(corf[2])}m█\033[m'
                    if p >= 0:
                        x += passo_x
                    else:
                        p += 2 * dx
                    y += passo_y

# cria tela
def cria_tela(y,x):
    global tela,largura,altura
    altura = y
    largura = x
    for c in range(0,altura):
        tela.append([])
        for r in range(0,largura):
            tela[c].append(' ')
# imprime tela
def imprime_tela():
    global tela
    for y in tela:
        for x in y:
            print(x,end=' ')
        print()
# trata terminal
def trata_terminal():
    time.sleep(0.016)
    # limpa terminal
    sys.stdout.write('\033[H')
    sys.stdout.flush()
    # some o cursor de digitação
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()