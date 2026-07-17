# biblioteca para controle do fps
from time import sleep, perf_counter
# biblioteca para limpar o terminal
import sys
# biblioteca para manter o buffer_de_desenho_original
from copy import deepcopy
# biblioteca para rotação
import math
# variáveis para o programa
# valores para camera
# estrutura de dados: [x, y]
rotacao_camera = [0,0]
# buffer de desenho
# estrutura de dados: [x,y,z,cor(se haverá cor)]
# -y cima, y baixo, o mesmo acontece com outras coordenadas


#    MODELOS
#   triãngulo
# [-4,4,1,True],
# [4,4,1,True],
# [4,4,1,True],
# [0,0,1,True],
# [0,0,1,True],
# [-4,4,1,True]
#      cubo
# [-2.5,2,1,True],
# [2.5,2,1,True],
# [2.5,-2,1,True],
# [-2.5,-2,1,True],
#
# [-2.5,2,1,True],
# [-2.5,-2,1,True],
# [2.5,2,1,True],
# [2.5,-2,1,True],
#
#
# [-2.5,2,2,True],
# [2.5,2,2,True],
# [2.5,-2,2,True],
# [-2.5,-2,2,True],
#
# [-2.5,2,2,True],
# [-2.5,-2,2,True],
# [2.5,2,2,True],
# [2.5,-2,2,True],
#
#
# [-2.5,2,1,True],
# [-2.5,2,2,True],
# [2.5,2,1,True],
# [2.5,2,2,True],
# [2.5,-2,1,True],
# [2.5,-2,2,True],
# [-2.5,-2,1,True],
# [-2.5,-2,2,True]
#    retângulo
# [-2.5,1,1,True],
# [2.5,1,1,True],
# [2.5,-1,1,True],
# [-2.5,-1,1,True],
#
# [-2.5,1,1,True],
# [-2.5,-1,1,True],
# [2.5,1,1,True],
# [2.5,-1,1,True],
#
#
# [-2.5,1,2,True],
# [2.5,1,2,True],
# [2.5,-1,2,True],
# [-2.5,-1,2,True],
#
# [-2.5,1,2,True],
# [-2.5,-1,2,True],
# [2.5,1,2,True],
# [2.5,-1,2,True],
#
#
# [-2.5,1,1,True],
# [-2.5,1,2,True],
# [2.5,1,1,True],
# [2.5,1,2,True],
# [2.5,-1,1,True],
# [2.5,-1,2,True],
# [-2.5,-1,1,True],
# [-2.5,-1,2,True]


buffer_de_desenho = \
[
[-2.5,1,1,True],
[2.5,1,1,True],
[2.5,-1,1,True],
[-2.5,-1,1,True],

[-2.5,1,1,True],
[-2.5,-1,1,True],
[2.5,1,1,True],
[2.5,-1,1,True],


[-2.5,1,2,True],
[2.5,1,2,True],
[2.5,-1,2,True],
[-2.5,-1,2,True],

[-2.5,1,2,True],
[-2.5,-1,2,True],
[2.5,1,2,True],
[2.5,-1,2,True],


[-2.5,1,1,True],
[-2.5,1,2,True],
[2.5,1,1,True],
[2.5,1,2,True],
[2.5,-1,1,True],
[2.5,-1,2,True],
[-2.5,-1,1,True],
[-2.5,-1,2,True]
]
# buffer de preservação de coordenadas originais
buffer_de_desenho_original = []
# buffer de aparência
# estrutura de dados: número(\033[ número m \033[m)
buffer_de_aparencia = [34,34,34,34,34,34,34,34,
                       34,34,34,34,34,34,34,34,
                       34,34,34,34,34,34,34,34
                       ]
# buffer de aparência para linhas
# estrutura de dados: número(\033[ número m \033[m)
buffer_de_aparencia_linha = [31]
# buffer para posição dos pixels das linhas
buffer_posicao_pixel = []
# configurações para iluminação, e shaders de iluminação
configuracoes_iluminacao = {'ativado':False,
                           'cor':36,
                           'direcao':-1,
                           'eixo':'x',
                           'alcance':9,
                           'reflexão':True}
# shader de fundo
shader_fundo = [34,True]
# variáveis para projeção
w = 16
h = 10
# buffer para o z-buffer da tela
z_buffer = []
# matrix para tela
tela = [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
         ]
# ---------------------------------------------------------------------------------------------------------------------------------------
# LSN-Linguagem de shader do RenderNatan
# função para tratamento de casos
def trata_condicionais(valor1,comparacao,valor2):
    classificador = False
    if comparacao == '=':
        if valor1 == valor2:
            classificador = True
    if comparacao == '<':
        if valor1 < valor2:
            classificador = True
    if comparacao == '>':
        if valor1 > valor2:
            classificador = True
    if comparacao == '~':
        if valor1 != valor2:
            classificador = True
    return classificador
# função para procura de caractere
def procura_caractere(string,marco,procurado):
    achou = False
    verificacao = False
    for v in string:
        if v == marco:
            achou = True
        if v == procurado and achou == True:
            verificacao = True
    return verificacao
# função para compilação de código LSN(Linguagem de Shader do RenderNatan)
def compila_codigo_lsn(codigo,pixel,x,y):
    '''
            SUMÁRIO DA LSN
    
    VARIÁVEIS INTERNAS :
    - pr:valor do pixel a ser retornado pelo shader, pode receber novos valores, o seu valor nunca pode ser ' '.
    - p:valor do pixel recebido que pode ser atribuído ao pr, para não mudar o que será retornado.
    - cp:valor para a cor do pixel, recomendado que receba um valor pelo programador.
    OPERAÇÕES MATEMÁTICAS :
    - s: ínicio para a soma dos valores positivos escolhidos
    - v: ínicio para a soma dos valores negativos escolhidos
    CONDICIONAIS :
    - cs: verifica se algo é verdade , se sim faz certa coisa se não faz nada
    '''
    # variáveis internas
    pixel_retorna = ' '
    cor_pixel = 0
    #
    ativacao_if = False
    linha = ''
    # loop para procura de linhas
    for c in codigo.strip():
        if c != ';':
            linha+=c
        elif c == ';':
            linha = linha.strip()
            # inseri um valor para pr
            if linha.startswith('pr=') or linha.startswith('pr ='):
                if procura_caractere(linha,'=','p'):
                    pixel_retorna = pixel
                else:
                    if linha[linha.find('=')] != linha[-1]:
                        if linha[linha.find('=') + 1] == ' ':
                            pixel_retorna = linha[linha.find('=') + 2]
                        else:
                            pixel_retorna = linha[linha.find('=') + 1]
            # inseri um valor para cp
            if linha.startswith('cp=') or linha.startswith('cp ='):
                if linha[linha.find('=')] != linha[-1]:
                    cor_pixel = linha[linha.find('=')+1:]
            # subtrai os valores para simular uma soma de valores positivos
            if linha.startswith('s'):
                operacao,valor1,valor2 = linha.split(' ')
                if valor1 == 'x':
                    x = x-int(valor2)
                elif valor1 == 'y':
                    y = y-int(valor2)
            # soma os valores para simular uma soma de valores negativos
            if linha.startswith('v'):
                operacao,valor1,valor2 = linha.split(' ')
                if valor1 == 'x':
                    x = x+int(valor2)
                elif valor1 == 'y':
                    y = y+int(valor2)
            if linha.startswith('cs'):
                caso = linha.split(' ')
                if caso[1] == 'y':
                    ativacao_if = trata_condicionais(y,caso[2],int(caso[3]))
                elif caso[1] == 'x':
                    ativacao_if = trata_condicionais(x,caso[2],int(caso[3]))
            # inseri um valor para pr
            if linha.startswith('$pr=') or linha.startswith('$pr ='):
                if ativacao_if == True:
                    if procura_caractere(linha,'=','p'):
                        pixel_retorna = pixel
                    else:
                        if linha[linha.find('=')] != linha[-1]:
                            if linha[linha.find('=') + 1] == ' ':
                                pixel_retorna = linha[linha.find('=') + 2]
                            else:
                                pixel_retorna = linha[linha.find('=') + 1]
            # inseri um valor para cp
            if linha.startswith('$cp=') or linha.startswith('$cp ='):
                if ativacao_if == True:
                    if linha[linha.find('=')] != linha[-1]:
                        cor_pixel = linha[linha.find('=') + 1:]
            # acaba com condicional
            if linha.startswith('ec'):
                if ativacao_if == True:
                    ativacao_if = False
            linha = ''
    return [f'\033[{cor_pixel}m{pixel_retorna}\033[m',x,y]

# função para utilização de código LSN(Linguagem de Shader do RenderNatan)
def utiliza_codigo_lsn(codigo):
    global tela,h,w
    # PASSOS:Criar loop que roda a tela inteira rodando , e para cada pixel(célula) rodar o shader em LSN
    for pos0,a in enumerate(tela):
        for pos1,c in enumerate(a):
            # verifica se não contém nada
            if c != ' ':
                # compila o código LSN
                c_novo = compila_codigo_lsn(codigo,c,pos1,pos0)
                # atualiza com o resultado do shader o pixel
                if abs(int(c_novo[2])) <= h and abs(int(c_novo[1])) <= w:
                    tela[pos0][pos1] = ' '
                    tela[abs(int(c_novo[2]))][abs(int(c_novo[1]))] = c_novo[0]

# função para rotação no eixo x
def rotacao_x(buffer,angulo):
    buffer_rotacionado = []
    cosseno = math.cos(math.radians(angulo))
    seno = math.sin(math.radians(angulo))
    for c in buffer:
        # estrutura de dados: [x,y,z,cor(se haverá cor)]
        buffer_rotacionado.append([c[0],
                                   c[1]*cosseno-c[2]*seno,
                                   c[1]*seno+c[2]*cosseno,
                                   c[3]])
    return buffer_rotacionado
# função para rotação no eixo y
def rotacao_y(buffer,angulo):
    buffer_rotacionado = []
    for c in buffer:
        cosseno = math.cos(math.radians(angulo))
        seno = math.sin(math.radians(angulo))
        # estrutura de dados: [x,y,z,cor(se haverá cor)]
        buffer_rotacionado.append([c[0]*cosseno+c[2]*seno,
                                   c[1],
                                   -c[0]*seno+c[2]*cosseno,
                                   c[3]])
    return buffer_rotacionado
# função para rotação no eixo z
def rotacao_z(buffer,angulo):
    buffer_rotacionado = []
    for c in buffer:
        cosseno = math.cos(math.radians(angulo))
        seno = math.sin(math.radians(angulo))
        # estrutura de dados: [x,y,z,cor(se haverá cor)]
        buffer_rotacionado.append([c[0]*cosseno-c[1]*seno,
                                   c[0]*seno+c[1]*cosseno,
                                   c[2],
                                   c[3]])
    return buffer_rotacionado
# função para uso do shader de reflexão
def shader_reflexao(coordenada,caractere_inicio):
    global configuracoes_iluminacao
    if abs(configuracoes_iluminacao['alcance']-coordenada) > 1 and configuracoes_iluminacao['reflexão'] == True:
        if abs(configuracoes_iluminacao['alcance']-coordenada) <= 3:
            caractere_inicio = '@'
    return caractere_inicio
# função para controle de iluminação
def tratamento_iluminacao(x,y,caractere):
    global configuracoes_iluminacao,h,w
    if configuracoes_iluminacao['ativado'] == True:
        if int(x) < w and int(y) < h:
            # verefica e se a vereficação for válida a iluminação será utilizada , este bloco serve para o eixo x
            if configuracoes_iluminacao['eixo'] == 'x':
                if x <= configuracoes_iluminacao['alcance'] and configuracoes_iluminacao['direcao'] > 0:
                    # shader de reflexão
                    caractere = shader_reflexao(x,caractere)
                    if abs(configuracoes_iluminacao['alcance']-x) == 0:
                        caractere = ':'
                    tela[int(y)][int(x)] = f'\033[{configuracoes_iluminacao['cor']}m{caractere}\033[m'
                if x >= configuracoes_iluminacao['alcance'] and configuracoes_iluminacao['direcao'] < 0:
                    # shader de reflexão
                    caractere = shader_reflexao(x,caractere)
                    if abs(configuracoes_iluminacao['alcance']-x) == 0:
                        caractere = ':'
                    tela[int(y)][int(x)] = f'\033[{configuracoes_iluminacao['cor']}m{caractere}\033[m'
            # verefica e se a vereficação for válida a iluminação será utilizada , este bloco serve para o eixo y
            if configuracoes_iluminacao['eixo'] == 'y':
                if y <= configuracoes_iluminacao['alcance'] and configuracoes_iluminacao['direcao'] > 0:
                    # shader de reflexão
                    caractere = shader_reflexao(y,caractere)
                    if abs(configuracoes_iluminacao['alcance']-y) == 0:
                        caractere = ':'
                    tela[int(y)][int(x)] = f'\033[{configuracoes_iluminacao['cor']}m{caractere}\033[m'
                if y >= configuracoes_iluminacao['alcance'] and configuracoes_iluminacao['direcao'] < 0:
                    # shader de reflexão
                    caractere = shader_reflexao(y,caractere)
                    if abs(configuracoes_iluminacao['alcance']-y) == 0:
                        caractere = ':'
                    tela[int(y)][int(x)] = f'\033[{configuracoes_iluminacao['cor']}m{caractere}\033[m'
# função para estilização com linha
def linha_estilizacao():
    print(30*'-')
# estados do renderizador
def estado_render():
    global buffer_de_desenho,rotacao_camera,buffer_de_aparencia,buffer_de_aparencia_linha
    linha_estilizacao()
    print('\033[36m ESTADOS DO RENDERIZADOR RENDERNATAN\033[m')
    print(f'\033[33mQuantidade de vértices no buffer_de_desenho\033[m: {len(buffer_de_desenho)}')
    print(f'\033[31mQuantidade de sub-shaders no buffer_de_aparencia\033[m: {len(buffer_de_aparencia)}')
    print(f'\033[34mQuantidade de valores de cor para as linha:\033[m: {len(buffer_de_aparencia_linha)}')
    print(f'\033[36mPosição da câmera\033[m: x:{rotacao_camera[0]}; y:{rotacao_camera[1]}')
    linha_estilizacao()
# função para atualização do z-buffer
def z_buffer_atualizacao(x,y,z):
    global z_buffer
    achou = False
    for pos,v in enumerate(z_buffer):
        if v[0] == x and v[1] == y and v[2] < z:
            achou = True
    return achou
# função para inserir novos valores nas coordenadas
def coordenadas_camera_transformadas():
    global rotacao_camera,buffer_de_desenho,buffer_de_desenho_original
    buffer_de_desenho_original = deepcopy(buffer_de_desenho)
    for cod in buffer_de_desenho:
        cod[0] -= rotacao_camera[0]
        cod[1] -= rotacao_camera[1]
# função para obter as coordenadas do objeto na tela
def coordenadas_transformadas(buffer,começo=0):
    global w, h
    termino = len(buffer)
    buffer_de_desenho_transformado = []
    for c in buffer[começo:termino]:
        # estrutura de dado: [x_tela , y_tela , cor , z(para z-buffer)]
        if c[2] > 0:
            buffer_de_desenho_transformado.append([((c[0])/c[2]) + (w/2),
                                                   ((c[1]) / c[2]) + (h/2),c[3],c[2]])
    return buffer_de_desenho_transformado
# função para linha
def linha(tipo,quant):
    if tipo == 1:
        print(quant*'-')
    elif tipo == 2:
        print(quant*'-=')
# funções para atualização de tela
# função para pontos
def atualiza_tela_pontos(buffer_transformado):
    global tela,buffer_de_aparencia,z_buffer,h,w
    for pos,c in enumerate(buffer_transformado):
        achou = z_buffer_atualizacao(c[0],c[1],c[3])
        if achou == False:
            if abs(int(c[1])) < h and abs(int(c[0])) < w and c[2] == True:
                tela[abs(int(c[1]))][abs(int(c[0]))] = f'\033[{buffer_de_aparencia[pos]}m.\033[m'
            if int(c[1]) < h and int(c[0]) < w and c[2] == False:
                tela[abs(int(c[1]))][abs(int(c[0]))] = '.'
            tratamento_iluminacao(abs(int(c[0])),abs(int(c[1])),'.')
            z_buffer.append([abs(int(c[0])),abs(int(c[1])),abs(int(c[3]))])
# função para linhas
def atualiza_tela_linhas(buffer_transformado,linhas_quant,pos_cor,começo,cor=False):
    global tela,z_buffer,h,w,buffer_posicao_pixel
    ponto1 = []
    ponto2 = []
    # obtenção dos vértices
    for pos,c in enumerate(buffer_transformado[começo:linhas_quant]):
        if pos % 2 == 0:
            ponto1.append(c)
        elif pos % 2 != 0:
            ponto2.append(c)
    # calculos para desenho de linha
    for pos, v in enumerate(ponto1):
        dx = abs(ponto2[pos][0] - v[0])
        dy = abs(ponto2[pos][1] - v[1])
        passo_x = 0
        if v[0] < ponto2[pos][0]:
            passo_x = 1
        else:
            passo_x = -1

        passo_y = 0
        if v[1] < ponto2[pos][1]:
            passo_y = 1
        else:
            passo_y = -1

        x = v[0]
        y = v[1]

        if dx > dy:
            p = 2 * dy - dx
            while abs(int(x)) != int(abs(ponto2[pos][0])):
                if abs(int(y)) < h and abs(int(x)) < w:
                    achou = z_buffer_atualizacao(x, y, v[3])
                    if achou == False:
                        if cor == False:
                            tela[abs(int(y))][abs(int(x))] = '.'
                        else:
                            tela[abs(int(y))][abs(int(x))] = f'\033[{buffer_de_aparencia_linha[pos_cor]}m.\033[m'
                        tratamento_iluminacao(abs(int(x)), abs(int(y)), '.')
                        z_buffer.append([int(abs(x)), int(abs(y)), v[3]])
                        buffer_posicao_pixel.append([x, y, v[3]])
                if p >= 0:
                    y += passo_y
                    p += 2 * (dy - dx)
                else:
                    p += 2 * dy
                x += passo_x
        else:
            p = 2 * dx - dy
            while abs(int(y)) != abs(int(ponto2[pos][1])):
                if abs(int(y)) < h and abs(int(x)) < w:
                    achou = z_buffer_atualizacao(x, y, v[3])
                    if achou == False:
                        if cor == False:
                            tela[abs(int(y))][abs(int(x))] = '.'
                        else:
                            tela[abs(int(y))][abs(int(x))] = f'\033[{buffer_de_aparencia_linha[pos_cor]}m.\033[m'
                        tratamento_iluminacao(abs(int(x)), abs(int(y)), '.')
                        z_buffer.append([abs(int(x)), abs(int(y)), v[3]])
                        buffer_posicao_pixel.append([x, y, v[3]])
                if p >= 0:
                    x += passo_x
                else:
                    p += 2 * dx
                y += passo_y
    return len(buffer_posicao_pixel)
# captura o menor valor y do buffer de posição para pixels de linhas
def y_maior():
    global buffer_posicao_pixel
    if len(buffer_posicao_pixel) != 0:
        maior = buffer_posicao_pixel[0][1]
        for c in buffer_posicao_pixel:
            if c[1] > maior:
                maior = c[1]
        return maior
# função para preencher as formas
def preenche_forma(cor1,cor2,começo,termino,shader):
    global buffer_de_desenho,buffer_posicao_pixel,h,w,tela,z_buffer
    if len(buffer_de_desenho) >= 6:
        pixels_forma = buffer_posicao_pixel[começo:termino]
        if pixels_forma:
            lista_x = []
            lista_y = []

            for pos,c in enumerate(pixels_forma):
                lista_x.append(c[0])
                lista_y.append(c[1])

                menor_x = int(max(0, min(lista_x)))
                maior_x = int(min(w - 1, max(lista_x)))
                menor_y = int(max(0, min(lista_y)))
                maior_y = int(min(h - 1, max(lista_y)))

                linhas_x = {}
                for v in range(menor_y,maior_y+1):
                    linhas_x[v] = []
                for p in pixels_forma:
                    px,py = int(p[0]), int(p[1])
                    if menor_y <= py <= maior_y:
                        linhas_x[py].append(px)
                testurizacao = True
                caractere = shader
                for y in range(menor_y,maior_y+1):
                    x_inicio = max(menor_x,min(linhas_x[y]))
                    x_fim = min(maior_x, max(linhas_x[y]))
                    for x in range(x_inicio,x_fim+1):
                        z_atual = pixels_forma[0][2]

                        if not z_buffer_atualizacao(abs(int(x)),abs(int(y)),z_atual):
                            if abs(int(y)) < h and abs(int(x)) < w:
                                if testurizacao == True:
                                    tela[y][x] = f'\033[{cor1}m{caractere}\033[m'
                                    testurizacao = False
                                elif testurizacao == False:
                                    tela[y][x] = f'\033[{cor2}m{caractere}\033[m'
                                    testurizacao = True
                                tratamento_iluminacao(abs(int(x)),abs(int(y)),'#')
                                z_buffer.append([abs(int(x)),abs(int(y)),z_atual])
        '''# valor para limite
        maior = y_maior()
        # rodar todo o buffer para as posições dos pixeis
        for px in buffer_posicao_pixel[começo:termino]:
            # contador para terminar o loop e marcar base do objeto
            cont = 0
            # loop para desenhar '#' até a base do objeto
            testurizacao = True
            caractere = shader
            while cont < int(abs(maior)) and abs(int(px[1]+cont)) < h and abs(int(px[0])) < w and abs(int(px[1]+cont)) <= int(abs(maior)):
                achou = z_buffer_atualizacao(int(px[0]), int(px[1] + cont), px[2])
                if achou == False:
                    achou2 = False
                    for v in buffer_posicao_pixel:
                        if v[1] == abs(int(px[1]+cont)) and abs(int(v[1])) != abs(int(maior)) and v[1] - abs(int(px[1]+cont)) != 0:
                            achou2 = True
                    if achou2 == True:
                        if testurizacao == True:
                            tela[abs(int(px[1]+cont))][abs(int(px[0]))] = f'\033[{cor1}m{caractere}\033[m'
                            testurizacao = False
                        elif testurizacao == False:
                            tela[abs(int(px[1] + cont))][abs(int(px[0]))] = f'\033[{cor2}m{caractere}\033[m'
                            testurizacao = True
                        tratamento_ilumicao(abs(int(px[0])), abs(int(px[1]+cont)),'#')
                        z_buffer.append([abs(int(px[0])),abs(int(px[1]+cont)),px[2]])
                cont += 1'''
# utiliza o shader de fundo para pintar o fundo
def pintar_fundo_shader():
    global shader_fundo,tela
    if shader_fundo[1] == True:
        for pos,c in enumerate(tela):
            for pos1,v in enumerate(c):
                if v == ' ':
                    tela[pos][pos1] = f'\033[0;0;{shader_fundo[0]}m*\033[m'
# função de desenho
def desenho_tela():
    global tela, buffer_de_desenho_original, buffer_de_desenho
    linha(2, 16)
    for c in tela:
        for v in c:
            print(v, end=' ')
        print()
    linha(2, 16)
    buffer_de_desenho = deepcopy(buffer_de_desenho_original)
# limpa o buffer colocado na tela
def limpa_tela_buffer():
    global tela
    for pos0,c in enumerate(tela):
        for pos1,v in enumerate(c):
            tela[pos0][pos1] = ' '
# limpa o buffer de pixels das linhas
def limpa_pixels_linhas_buffer():
    global buffer_posicao_pixel
    buffer_posicao_pixel = []
# limpa o z-buffer
def limpa_z_buffer():
    global z_buffer
    z_buffer = []
# função principal, onde tudo acontece
def main():
    global buffer_de_desenho,rotacao_camera
    # mostra estado
    estado_render()
    sleep(4)
    # limpa terminal
    sys.stdout.write("\033c")
    sys.stdout.flush()
    # some o cursor de digitação
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()
    coordenadas_camera_transformadas()
    objeto_retangulo = deepcopy(buffer_de_desenho)
    # código LSN
    codigo_lsn = '''
                  pr=@;
                  cp=31;
                  cs x ~ 8 ;
                  $cp=36;
                  ec;
                  '''
    #
    # RECOMENDAÇÃO: Rode o código no terminal para melhor performance , cuidado ao rodar no Pycharm dependendo da sua configuração
    #
    while True:
        # pineline => transforma o buffer de desenho em relação a cãmera=> carrega o buffer de desenho => utiliza o buffer de desenho para
        # desenhar os vértices => utiliza o buffer de desenho com base para conectar linhas => utiliza as coordenadas das linhas
        # para preencher formas => utiliza o shader de fundo para pintar o fundo => limpa os buffers de tela e das linhas => limpa a
        # tela e controla o fps
        # CUIDADO: não utilize rotações antes de transformar as coordenadas tridimensionais em bidimensionais,
        # processos especiais => iluminação => testurização simples
        # modifica e utiliza os buffers
        começo = perf_counter()
        # 0.000216
        buffer = coordenadas_transformadas(rotacao_z(objeto_retangulo,45))
        # 0.000042
        atualiza_tela_pontos(buffer)
        pixels_usados = atualiza_tela_linhas(buffer,12,0,0,True)
        # 0.000174
        print(pixels_usados)
        preenche_forma(31,33,0,pixels_usados,'=')
        # 0.000514
        utiliza_codigo_lsn(codigo_lsn)
        #
        pintar_fundo_shader()
        desenho_tela()
        limpa_pixels_linhas_buffer()
        limpa_tela_buffer()
        limpa_z_buffer()
        # 0.000038
        #
        # controla o fps - para 60 fps
        sleep(0.016)
        # limpa terminal
        sys.stdout.write("\033[H")
        sys.stdout.flush()
        # some o cursor de digitação
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()
        # 0.001730
        fim = perf_counter()
        print(f'{fim-começo:.6f}')
main()