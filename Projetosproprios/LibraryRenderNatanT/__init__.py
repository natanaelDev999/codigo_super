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
# biblioteca para trabalhar com vetores
import LibraryVectorNatan as lvn
# biblioteca para manipulação de tempo
import time
# compilador TelShader
from LibraryRenderNatanT.compilador_TelShader import compila_codigo_TelShader
###############################################################
#                         buffers
# Buffer de Dados para Vértices(BDV)
bdv = []
# Buffer de Dados para Aparência(BDA)
bda = []
###############################################################
#                          tela
tela = []
z_buffer = []
largura = 0
altura = 0
###############################################################
#                     FUNÇÕES PARA SHADERS
def compila_codigo_telshader(codigo):
    global tela
    for pos0, c in enumerate(tela):
        for pos1, p in enumerate(c):
            if p != ' ':
                tela[pos0][pos1] = ' '
                pixel = compila_codigo_TelShader(codigo, p, pos1, pos0)
                if pixel[2] < altura and pixel[1] < largura:
                    tela[pixel[2]][pixel[1]] = pixel[0]
                    print(tela[pixel[2]][pixel[1]])
###############################################################
#                     FUNÇÕES UTILITÁRIAS
# trata z-buffer
def trata_z_buffer(x,y,z):
    global z_buffer
    resposta = True
    if z_buffer[y][x] != None:
        if z_buffer[y][x] < z:
            resposta = False
    return resposta
# função para adicionar dados aos bufffers
def adiciona_dados(tipo,dados):
    global bdv,bda
    if len(dados) > 0:
        if tipo == "BDV" or tipo == "Buffer de Dados para Vértices":
            bdv = dados
        elif tipo == "BDA" or tipo == "Buffer de Dados para Aparência":
            bda = dados
# projeta vértices
def projeta_vertices(desenha_pontos=False):
    global bdv,largura,altura,bda
    proj = []
    for pos0,p in enumerate(bdv):
        if p[2] > 0:
            proj.append([int((p[0]/p[2])+(largura/2)),
                         int((p[1]/p[2])+(altura/2)),pos0,p[2]])
            if desenha_pontos == True:
                if (p[0] / p[2]) + (largura / 2) < largura and (p[1] / p[2]) + (altura / 2) < altura:
                    if pos0 < len(bda):
                        if trata_z_buffer(int((p[0]/p[2])+(largura/2)),int((p[1]/p[2])+(altura/2)),p[2]) == True:
                            tela[int((p[1]/p[2])+(altura/2))][int((p[0]/p[2])+(largura/2))] = f'\033[38;2;{bda[pos0][0]};{bda[pos0][1]};{bda[pos0][2]}m█\033[m'
                            z_buffer[int((p[1]/p[2])+(altura/2))][int((p[0]/p[2])+(largura/2))] = p[2]
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
                        if trata_z_buffer(x,y,v[2]):
                            corf = lvn.divide_vetores(lvn.soma_vetores(cor1, cor2), [x, y, 2])
                            tela[y][x] = f'\033[38;2;{int(corf[0])};{int(corf[1])};{int(corf[2])}m█\033[m'
                            z_buffer[y][x] = v[3]
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
                        if trata_z_buffer(x, y, v[2]):
                            corf = lvn.divide_vetores(lvn.soma_vetores(cor1,cor2),[x,y,1])
                            tela[y][x] =  f'\033[38;2;{int(corf[0])};{int(corf[1])};{int(corf[2])}m█\033[m'
                            z_buffer[y][x] = v[3]
                    if p >= 0:
                        x += passo_x
                    else:
                        p += 2 * dx
                    y += passo_y
#TRIÂNGULO FUNÇÕES
def perpendicular(vetor):
    return [vetor[1],-vetor[0]]

def ponto_teste_dentro(a,b,p):
    ap = [p[0] - a[0],p[1]-a[1]]
    abPerp = perpendicular([b[0]-a[0],b[1]-a[1]])
    return lvn.produto_escalar2(ap,abPerp) >= 0

def ponto_triangulo(a,b,c,p):
    sideAB = ponto_teste_dentro(a,b,p)

    sideBC = ponto_teste_dentro(b,c,p)

    sideCA = ponto_teste_dentro(c,a,p)

    return sideAB and sideBC and sideCA

def desenha_triangulo(proj,comeco,fim,cor):
    global tela,largura,altura,bda

    if len(proj) % 3 == 0:
        p = []
        for c in proj[comeco:fim]:
            if len(p) != 3:
                p.append(c)
            if len(p) == 3:

                y_max = max(p[0][1],p[1][1],p[2][1])+1
                y_min = min(p[0][1],p[1][1],p[2][1])+1

                x_max = max(p[0][0],p[1][0],p[2][0])+1
                x_min = min(p[0][0],p[1][0],p[2][0])+1

                ciclosy = 0
                ciclosx = 0
                for y in range(y_min,y_max):
                    ciclosy +=1
                    for x in range(x_min,x_max):
                        ciclosx += 1
                        if ponto_triangulo(p[0],p[1],p[2],[x,y]) == True:
                            if trata_z_buffer(x,y,p[0][3]) == True:
                                tela[y][x] = f'\033[38;2;{cor[0]};{cor[1]};{cor[2]}m█\033[m'
                                z_buffer[y][x] = (p[0][3]+p[1][3]+p[2][3])/3

# cria tela e z-buffer
def cria_tela(y,x):
    global tela,largura,altura,z_buffer
    altura = y
    largura = x
    for c in range(0,altura):
        tela.append([])
        z_buffer.append([])
        for r in range(0,largura):
            tela[c].append(' ')
            z_buffer[c].append(None)

# imprime tela
def imprime_tela():
    global tela,largura,altura
    for y in range(altura):
        for x in range(largura):
            print(tela[y][x],end=' ')
        print()

# limpa tela e z_buffer
def limpa_tz():
    global tela,z_buffer
    for pos0,c in enumerate(tela):
        for pos1,v in enumerate(c):
            tela[pos0][pos1] = ' '
            z_buffer[pos0][pos1] = None

# trata terminal
def trata_terminal(fps):
    limpa_tz()
    if fps == 1:
        time.sleep(0.016)
    elif fps == 2:
        time.sleep(0.008)
    elif fps == 3:
        time.sleep(0.004)
    # limpa terminal
    sys.stdout.write('\033[H')
    sys.stdout.flush()
    # some o cursor de digitação
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()