###############################################################
#                     LibraryRenderNatanT
###############################################################
# criação do projeto: 18/09/2026
# termino do projeto:
# intervalo de tempo:
###############################################################
# DADOS DOS SHADERS
# criação do TelShader: 20/09/2026
# criação do TelTShader: 29/09/2026
# criação do TelMatrixShader: 01/10/2026
# criação do TelComputerShader: 20/10/2026
###############################################################
#                         PIPELINE
#Inicialização -> carrega dados -> cria tela -> cria buffer
#adicional(opcional) ou execução do TelMatrixShader

#Renderização -> TelMatrixShader -> projeção dos vértices ->
#desenha linha -> desenha triângulos -> TelShader -> TelTShader

#TelComputerShader: entrada -> TelComputerShader -> saída
###############################################################
#                 bibliotecas utilizadas
# biblioteca para manipulação do terminal
import sys
# biblioteca para trabalhar com vetores
import LibraryVectorNatan as lvn
# biblioteca para manipulação de tempo
import time
# compilador TelShader e do TelTShader
from LibraryRenderNatanT.compilador_TelShader import compila_codigo_telshader
# compilador TelMatrixShader
from LibraryRenderNatanT.compilador_TelMatrixShader import compila_codigo_telmatrixshader
# compilador TelComputerShader
from LibraryRenderNatanT.compilador_TelComputerShader import compila_codigo_telcomputershader
# biblioteca para controle de memória
import psutil as pt
# biblioteca para controle de arquivos
import os
###############################################################
#                         buffers
# Buffer de Dados para Vértices(BDV)
bdv = []
#  Buffer reserva
bdv_c = []
# Buffer de Dados para Aparência(BDA)
bda = []
# Buffer de Dados para Matrizes(BDM)
bdm = {"0":[],"1":[],"2":[],"3":[],"4":[],"5":[],"6":[],"7":[],"8":[],'9':[],'10':[],'11':[],'12':[],'13':[],
            '14':[],'15':[],'16':[]}
# Lista para Buffers Adicionais(LBA)
lba = []
###############################################################
#                          tela
tela = []
# tela reserva
tela_c = []
z_buffer = []
largura = 0
altura = 0
###############################################################
#                 CARREGA ARQUIVOS DE CÓDIGO
def carrega_arquivo(caminho):
    if not os.path.basename(caminho).endswith('.ns') == True:
        return ''
    arquivo1 = open(caminho,'r')
    arquivo1.seek(0)

    arquivo_codigo = str(arquivo1.read())

    arquivo1.close()

    return arquivo_codigo
###############################################################
#              CRIAÇÃO DE BUFFERS ADICIONAIS E MAIS
def captura_posicao_buffer(nome):
    global lba
    for pos0,b in enumerate(lba):
        if b[0] == nome:
            return pos0
def cria_buffer_adicional(nome,tamanho):
    global lba
    # 56 -> valor inicial que ocupa uma lista
    # 8 -> tamanho de um ponteiro(que é o que guarda uma lista)
    memoria_utilizada_buffer = 56+(tamanho*8)
    mem_info = pt.virtual_memory()
    # verifica se o tamanho do buffer é menor do que metade da memória disponível
    if mem_info.available / 2 > memoria_utilizada_buffer:
        lba.append([nome,[],tamanho])
def adiciona_valor_buffer(nome,valor):
    global lba
    if type(valor) == dict:
        return
    for pos0,b in enumerate(lba):
        if b[0] == nome and len(b[1]) < b[2]:
            lba[pos0][1].append(valor)
            break
def retira_valor_buffer(nome,pos):
    global lba
    for pos0,b in enumerate(lba):
        if b[0] == nome and len(b[1]) > pos and pos < b[2]:
            del lba[pos0][1][pos]
def copia_buffer(nome1,nome2,fim,comeco=0):
    global lba
    for pos0, b1 in enumerate(lba):
        if b1[0] == nome1:
            for pos1, b2 in enumerate(lba):
                if b2[0] == nome2 and b1[2] == b2[2]:
                    lba[pos0][1] = lba[pos1][1][comeco:fim+1]
                    break
            break
def apaga_buffer(nome):
    global lba
    for pos0,b in enumerate(lba):
        if b[0] == nome:
            del lba[pos0]
            break
###############################################################
#                     FUNÇÕES PARA SHADERS
# TelShader
def compila_codigo_TelShader(codigo,rec=False,pos=0,modo_armazenamento=''):
    global tela,bdm

    tela_original = []
    for v in tela:
        tela_original.append(v)

    for i in tela:
        for j in tela:
            j = ' '

    for pos0, linha in enumerate(tela_original):
        for pos1, p in enumerate(linha):
            if p != ' ':
                tela[pos0][pos1] = ' '
                pixel = compila_codigo_telshader(codigo,p,pos1,pos0,bdm,rec,pos,lba,modo_armazenamento)

                if 0 <= pixel[2] < altura and 0 <= pixel[1] < largura:
                    tela[pixel[2]][pixel[1]] = pixel[0]
# TelTShader
def compila_codigo_TelTShader(codigo,rec=False,pos=0,modo_armazenamento=''):
    global tela

    tela_original = []
    for v in tela:
        tela_original.append(v)

    for i in tela:
        for j in tela:
            j = ' '

    for pos0, linha in enumerate(tela_original):
        for pos1, p in enumerate(linha):
            if p == ' ':
                tela[pos0][pos1] = ' '
                pixel = compila_codigo_telshader(codigo, p, pos1, pos0, bdm,rec,pos,lba,modo_armazenamento)

                if 0 <= pixel[2] < altura and 0 <= pixel[1] < largura:
                    tela[pixel[2]][pixel[1]] = pixel[0]
# TelMatrixShader
def compila_codigo_TelMatrixShader(codigo,tipo,rec=False,pos=0,modo_armazenamento=''):
    global tela, altura, largura,lba
    if tipo == "BDV" or tipo == "Buffer de Dados para Vértices":
        for pos0,c in enumerate(bdv):
            bdv[pos0] = compila_codigo_telmatrixshader(codigo,c,bdm,rec,pos,lba,modo_armazenamento)
    elif tipo == "BDA" or tipo == "Buffer de Dados para Aparência":
        for pos0,c in enumerate(bda):
            bda[pos0] = compila_codigo_telmatrixshader(codigo,c,bdm,rec,pos,lba,modo_armazenamento)
# TelComputerShader
def compila_codigo_TelComputerShader(codigo,entrada,grupos,veref):
    global tela,lba,z_buffer
    saida = []
    # o shader receberá o valor de entrada, sua posição na matriz de Workgroups
    if type(entrada) == str:
        if entrada == 'TexO':
            entrada = tela[:]
        elif entrada == 'TexZ':
            entrada = z_buffer[:]
    # se entrada for do tipo int , será considerada como o endereço de um buffer adicinonal
    elif type(entrada) == int:
        if entrada < len(lba):
            entrada = lba[entrada][1]
    # passa pela quantidade de Workgroups
    if len(grupos) == 1 and len(grupos) == len(veref):
        for py in range(grupos[0]):
            if py < veref[0]:
                tipo = ''

                if type(entrada[py]) == list:
                    tipo = 'list'

                entrada[py] = compila_codigo_telcomputershader(codigo,entrada[py],tipo,bdm,[py])

                saida.append(compila_codigo_telcomputershader(codigo,entrada[py],tipo,bdm,[py]))
    elif len(grupos) == 2 and len(grupos) == len(veref):
        for py in range(grupos[1]):
            saida.append([])
            for px in range(grupos[0]):
                if py < veref[0] and px < veref[1]:
                    tipo = ''
                    if type(entrada[py][px]) == list:
                        tipo = 'list'
                    entrada[py][px] = compila_codigo_telcomputershader(codigo,entrada[py][px],tipo,bdm,[px,py])
                    saida[py].append(compila_codigo_telcomputershader(codigo,entrada[py][px],tipo,bdm,[px,py]))
    elif len(grupos) == 3 and len(grupos) == len(veref):
        for pz in range(grupos[2]):
            saida.append([])
            for py in range(grupos[1]):
                saida[pz].append([])
                for px in range(grupos[0]):
                    if py < veref[1] and px < veref[0] and pz < veref[2]:
                        tipo = ''
                        if type(entrada[pz][py][px]) == list:
                            tipo = 'list'
                        entrada[pz][py][px] = compila_codigo_telcomputershader(codigo,entrada[pz][py][px],tipo,bdm,[px,py,pz])
                        saida[pz][py].append(compila_codigo_telcomputershader(codigo,entrada[pz][py][px],tipo,bdm,[px,py,pz]))
    return saida
###############################################################
#                     FUNÇÕES UTILITÁRIAS
# trata z-buffer
def trata_z_buffer(x,y,z):
    global z_buffer, largura, altura
    resposta = True
    if x < largura and y < altura and x > 0 and y > 0:
        if z_buffer[y][x] != None:
            if z_buffer[y][x] < z:
                resposta = False
    return resposta
# função para adicionar dados aos bufffers
def adiciona_dados(tipo,dados,pos=0):
    global bdv,bda,bdv_c
    if len(dados) > 0:
        if tipo == "BDV" or tipo == "Buffer de Dados para Vértices":
            bdv = dados
            bdv_c = bdv
        elif tipo == "BDA" or tipo == "Buffer de Dados para Aparência":
            bda = dados
        elif tipo == "BDM" or tipo == "Buffer de Dados para Matrizes":
            bdm[f"{pos}"] = dados
# projeta vértices
def projeta_vertices(dist,desenha_pontos=False,camera=False,campo_visao=0,direcao_camera=[0,0,1],posicao_camera=[0,0,0]):
    global bdv,largura,altura,bda
    proj = []
    for pos0,p in enumerate(bdv):
        if p[2] > 0 and len(p) == 3:
            if camera == True:
                if (lvn.angulo_vetores_graus(lvn.subtrai_vetores(p,posicao_camera),lvn.subtrai_vetores(direcao_camera,posicao_camera)) < campo_visao
                        and lvn.angulo_vetores_graus(lvn.subtrai_vetores(p,posicao_camera),lvn.subtrai_vetores(direcao_camera,posicao_camera)) > 0):
                    proj.append([int((p[0]/(p[2]+dist))+(largura/2)),
                                    int((p[1]/(p[2]+dist))+(altura/2)),pos0,p[2]])
                    # desenha pontos
                    if desenha_pontos == True:
                        if (p[0] / (p[2] + dist)) + (largura / 2) < largura and (p[1] / (p[2] + dist)) + (
                                altura / 2) < altura:
                            if pos0 < len(bda):
                                if trata_z_buffer(int((p[0] / (p[2] + dist)) + (largura / 2)),
                                                  int((p[1] / (p[2] + dist)) + (altura / 2)), p[2]) == True:
                                    tela[int((p[1] / (p[2] + dist)) + (altura / 2))][int((p[0] / (p[2] + dist)) + (
                                                largura / 2))] = f'\033[38;2;{bda[pos0][0]};{bda[pos0][1]};{bda[pos0][2]}m█\033[m'
                                    z_buffer[int((p[1] / (p[2] + dist)) + (altura / 2))][
                                        int((p[0] / (p[2] + dist)) + (largura / 2))] = p[2]
            else:
                proj.append([int((p[0] / (p[2] + dist)) + (largura / 2)),
                             int((p[1] / (p[2] + dist)) + (altura / 2)), pos0, p[2]])
                # desenha pontos
                if desenha_pontos == True:
                    if (p[0] / (p[2]+dist)) + (largura / 2) < largura and (p[1] / (p[2]+dist)) + (altura / 2) < altura:
                        if pos0 < len(bda):
                            if trata_z_buffer(int((p[0]/(p[2]+dist))+(largura/2)),int((p[1]/(p[2]+dist))+(altura/2)),p[2]) == True:
                                tela[int((p[1]/(p[2]+dist))+(altura/2))][int((p[0]/(p[2]+dist))+(largura/2))] = f'\033[38;2;{bda[pos0][0]};{bda[pos0][1]};{bda[pos0][2]}m█\033[m'
                                z_buffer[int((p[1]/(p[2]+dist))+(altura/2))][int((p[0]/(p[2]+dist))+(largura/2))] = p[2]
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

def desenha_triangulo(proj,comeco,fim,inter=False):
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

                for y in range(y_min,y_max):
                    for x in range(x_min,x_max):
                        if ponto_triangulo(p[0],p[1],p[2],[x,y]) == True:
                            if trata_z_buffer(x,y,p[0][3]) == True:
                                if y < altura and x < largura and y >= 0 and x >= 0:
                                    cor = []
                                    if inter == True:
                                        cor = lvn.multiplica_vetores(lvn.divide_vetores(
                                            lvn.subtrai_vetores(bda[p[1][2]],bda[p[2][2]]),
                                            lvn.subtrai_vetores(bda[p[0][2]],bda[p[1][2]]),
                                        ),
                                    [x*10,y*10,1])
                                    else:
                                        cor = bda[p[0][2]]
                                    tela[y][x] = f'\033[38;2;{cor[0]};{cor[1]};{cor[2]}m█\033[m'
                                    z_buffer[y][x] = (p[0][3]+p[1][3]+p[2][3])/3
                p = []


# preserva estado anterior dos dados
def preserva_dados():
    global tela, tela_c , bdv, bdv_c
    tela = tela_c.copy()
    bdv = bdv_c.copy()
# carrega novos dados
def carrega_novos_dados():
    global tela, tela_c , bdv, bdv_c
    tela_c = tela.copy()
    bdv_c = bdv.copy()
# limpa dados
def limpa_dados():
    global tela, bdv, bda
    tela = []
    bdv = []
    bda = []
# cria tela e z-buffer
def cria_tela(y,x):
    global tela,largura,altura,z_buffer,tela_c
    altura = y
    largura = x
    for c in range(0,altura):
        tela.append([])
        z_buffer.append([])
        for r in range(0,largura):
            tela[c].append(' ')
            z_buffer[c].append(None)
    tela_c = tela.copy()

# imprime tela
def imprime_tela():
    global tela,largura,altura
    for y in tela:
        for x in y:
            print(x,end=' ')
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