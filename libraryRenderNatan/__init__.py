###############################################################
#                   LibraryRenderNatan
###############################################################
# criação do projeto: 27/07/2026
###############################################################
#                 bibliotecas utilizadas
# biblioteca para manipulação do terminal
import sys
# biblioteca para manipulação de fps
import time
# biblioteca para matemática
import math
###############################################################
#                         buffers
# Buffer de Dados para Vértices(BDV)
buffer_de_vertices = []
# Buffer de Dados para Aparência(BDA)
buffer_de_aparencia = []
# Buffer de Dados para Matrizes(BDM)
buffer_de_matrizes = {'1':[],'2':[],'3':[],'4':[],'5':[],'6':[]}
###############################################################
#                      tela e z-buffer
tela = []
z_buffer = []
altura_tela = 0
largura_tela = 0
###############################################################
#                   FUNÇÕES MATEMÁTICAS
###############################################################
def multiplicacao_matricial(matriz,vetor):
    vetor_saida = []
    for c in matriz:
        soma = 0
        for pos, v in enumerate(c):
            soma += v * int(vetor[pos])
        vetor_saida.append(soma)
    return vetor_saida
###############################################################
#                   FUNÇÕES PARA A LTLN
###############################################################
# função para compilação de código LTLN(Linguagem de tela do RenderNatan)
def compila_codigo_LTLN(codigo,x,y):
    '''
            SUMÁRIO DA LTLN

    VARIÁVEIS INTERNAS :
    - pixel: representa o pixel a ser retornado.
    '''
    linha = ''
    pixel = ' '
    cor_pixel = 0
    ativacao_if = False
    for c in codigo:
        if c != ';':
            linha += c
        elif c == ';':
            linha = linha.strip()
            if linha.startswith('pr=') or linha.startswith('pr ='):
                comando, caractere = linha.split('=')
                pixel = caractere.strip()
            elif linha.startswith('cp=') or linha.startswith('cp ='):
                comando, cor = linha.split('=')
                cor_pixel = cor.strip()
            elif linha.startswith('cs'):
                caso = linha.split(' ')
                if caso[1] == 'y':
                    ativacao_if = trata_condicionais(y, caso[2], int(caso[3]))
                elif caso[1] == 'x':
                    ativacao_if = trata_condicionais(x, caso[2], int(caso[3]))
            elif linha.startswith('ec'):
                ativacao_if = False
            elif linha.startswith('$pr=') or linha.startswith('$pr ='):
                if ativacao_if == True:
                    comando, caractere = linha.split('=')
                    pixel = caractere.strip()
            elif linha.startswith('$cp=') or linha.startswith('$cp ='):
                if ativacao_if == True:
                    comando, cor = linha.split('=')
                    cor_pixel = cor.strip()
            linha = ''
    return f'\033[{cor_pixel}m{pixel}\033[m'
# função para utilização do código LTLN(linguagem de tela da libraryRenderNatan)
def utiliza_codigo_LTLN(codigo):
    global tela
    for pos0,c in enumerate(tela):
        for pos1,v in enumerate(c):
            if v == ' ':
                tela[pos0][pos1] = compila_codigo_LTLN(codigo,pos1,pos0)
###############################################################
#                   FUNÇÕES PARA A LMLN
###############################################################
# função para compilação de código LMLN(Linguagem de Matricial do RenderNatan)
def compila_codigo_LMLN(codigo,vetor):
    '''
            SUMÁRIO DA LMLN

    VARIÁVEIS INTERNAS :
    - v3: o vetor a ser retornado, tem comprimento de 3 inteiros x,y,z.
    FUNÇÕES MATRICIAIS :
    - MMV: multiplica um vetor por uma matriz do BDM.
    '''
    # variáveis auxiliares
    linha = ''
    estruturas_dados = {'vetores':[]}
    for c in codigo:
        if c != ';':
            linha += c
        elif c == ';':
            linha = linha.strip()
            # cria vetor
            if linha.startswith('t'):
                dados = linha.split(' ')
                if dados[1] != 'v3':
                    # verefica se existe outro vetor com outro nome
                    achou = False
                    for v in estruturas_dados['vetores']:
                        if v[0] == dados[1]:
                            achou = True
                    if achou == False:
                        estruturas_dados['vetores'].append([dados[1], dados[2:]])
            # faz uma multiplicação entre vetor e matriz
            if linha.startswith('MMV'):
                # sintaxe: comando índice vetor
                comando, indice, vetor1 = linha.split(' ')
                if len(buffer_de_matrizes) > 0:
                    if vetor1 == 'v3':
                        vetor_resultado = multiplicacao_matricial(buffer_de_matrizes[f'{indice}'], vetor)
                        if len(vetor_resultado) > 0:
                            vetor = vetor_resultado
                    else:
                        for pos, v in enumerate(estruturas_dados['vetores']):
                            if v[0] == vetor1:
                                vetor_resultado = multiplicacao_matricial(buffer_de_matrizes[f'{indice}'], v[1])
                                estruturas_dados['vetores'][pos][1] = vetor_resultado
            if linha.startswith('ot'):
                dados = linha.split(' ')
                if 'x' in dados[1] and 'y' in dados[1]:
                    for v in estruturas_dados['vetores']:
                        if v[0] == dados[2]:
                            if int(v[1][0]) <= largura_tela and int(v[1][1]) <= altura_tela:
                                vetor[0] = int(v[1][0])
                                vetor[1] = int(v[1][1])
                                vetor[2] = int(v[1][2])
                                break
            if linha.startswith('ts'):
                dados = linha.split(' ')
                if 'v3' in dados[1]:
                    for v in estruturas_dados['vetores']:
                        if v[0] == dados[2]:
                            if int(v[1][0]) + vetor[0] <= largura_tela and int(v[1][1]) + vetor[1] <= altura_tela:
                                vetor[0] += int(v[1][0])
                                vetor[1] += int(v[1][1])
                                vetor[2] += int(v[1][2])
                                break
            if linha.startswith('tp'):
                dados = linha.split(' ')
                if 'v3' in dados[1]:
                    for v in estruturas_dados['vetores']:
                        if v[0] == dados[2]:
                            if int(v[1][0]) + vetor[0] <= largura_tela and int(v[1][1]) + vetor[1] <= altura_tela:
                                vetor[0] -= int(v[1][0])
                                vetor[1] -= int(v[1][1])
                                vetor[2] -= int(v[1][2])
                                break
            linha = ''
    return vetor
# função para utilização do código LMLN(linguagem de matricial da libraryRenderNatan)
def utiliza_codigo_LMLN(codigo):
    global buffer_de_vertices
    for pos0,c in enumerate(buffer_de_vertices):
        buffer_de_vertices[pos0] = compila_codigo_LMLN(codigo,c)
###############################################################
#                   FUNÇÕES PARA A LSLN
###############################################################
# funções auxiliares para o código LSLN(linguagem de Sombreamento da libraryRenderNatan)
# procura dados
def procura_dados(procurado,local):
    achado = None
    for v in local['variáveis']:
        if v[0] == procurado:
            achado = v[1]
    return achado
# função para tratamento de casos
def trata_condicionais(valor1,comparacao,valor2):
    classificador = False
    if comparacao == '=':
        if valor1 == valor2:
            classificador = True
    elif comparacao == '<':
        if valor1 < valor2:
            classificador = True
    elif comparacao == '>':
        if valor1 > valor2:
            classificador = True
    elif comparacao == '~':
        if valor1 != valor2:
            classificador = True
    elif comparacao == '%2':
        if valor1 % valor2 == 0:
            classificador = True
    elif comparacao == '%+':
        if valor1 % valor2 != 0:
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
# função para compilação de código LSLN(Linguagem de Sombreamento do RenderNatan)
def compila_codigo_LSLN(codigo, pixel, x, y):
    '''
            SUMÁRIO DA LSLN

    VARIÁVEIS INTERNAS :
    - pr:valor do pixel a ser retornado pelo shader, pode receber novos valores, o seu valor nunca pode ser ' '.
    - p:valor do pixel recebido que pode ser atribuído ao pr, para não mudar o que será retornado.
    - cp:valor para a cor do pixel, recomendado que receba um valor pelo programador.
    OPERAÇÕES MATEMÁTICAS :
    - s: ínicio para a soma dos valores positivos escolhidos.
    - v: ínicio para a soma dos valores negativos escolhidos.
    CONDICIONAIS :
    - cs: verifica se algo é verdade , se sim faz certa coisa se não faz nada.
    VARIÁVEIS :
    - l: cria e salva na memória do pixel , uma variável.
    VETORES :
    - t: cria e salva na memória do pixel , um vetor.
    - ot: inseri um valor em x e y com base em um vetor.
    - ts: faz uma soma negativa nos valores x e y com base em um vetor.
    - tp: faz uma soma positiva nos valores x e y com base em um vetor.
    FUNÇÕES TRIGONOMÉTRICAS :
    - COS: faz uma operação com o cosseno de um ângulo
    - SIN: faz uma operação com o seno de um ângulo
    FUNÇÕES MATRICIAIS :
    - MMV: multiplica um vetor por uma matriz do BDM
    '''
    global largura_tela, altura_tela
    # variáveis internas
    pixel_retorna = ' '
    cor_pixel = 0
    #
    estruturas_dados = {'variáveis': [], 'vetores': []}
    ativacao_if = False
    linha = ''
    # loop para procura de linhas
    for c in codigo.strip():
        if c != ';':
            linha += c
        elif c == ';':
            if c != ';':
                linha += c
            elif c == ';' and not linha.startswith('//'):
                linha = linha.strip()
                # inseri um valor para pr
                if linha.startswith('pr=') or linha.startswith('pr ='):
                    if procura_caractere(linha, '=', 'p'):
                        pixel_retorna = pixel
                    else:
                        if linha[linha.find('=')] != linha[-1]:
                            vereficacao = procura_dados(linha[linha.find('=') + 1:], estruturas_dados)
                            if vereficacao == None:
                                if linha[linha.find('=') + 1] == ' ':
                                    pixel_retorna = linha[linha.find('=') + 2]
                                else:
                                    pixel_retorna = linha[linha.find('=') + 1]
                            elif vereficacao != None:
                                pixel_retorna = vereficacao
                # inseri um valor para cp
                if linha.startswith('cp=') or linha.startswith('cp ='):
                    vereficacao = procura_dados(linha[linha.find('=') + 1:], estruturas_dados)
                    if linha[linha.find('=')] != linha[-1] and vereficacao == None:
                        cor_pixel = linha[linha.find('=') + 1:]
                    elif vereficacao != None:
                        cor_pixel = vereficacao
                # subtrai os valores para simular uma soma de valores positivos
                if linha.startswith('s'):
                    operacao, valor1, valor2 = linha.split(' ')
                    if valor1 == 'x':
                        x = x - int(valor2)
                    elif valor1 == 'y':
                        y = y - int(valor2)
                # subtrai os valores para simular uma soma de valores positivos
                if linha.startswith('$s'):
                    if ativacao_if == True:
                        operacao, valor1, valor2 = linha.split(' ')
                        if valor1 == 'x':
                            x = x - int(valor2)
                        elif valor1 == 'y':
                            y = y - int(valor2)
                # soma os valores para simular uma soma de valores negativos
                if linha.startswith('v'):
                    operacao, valor1, valor2 = linha.split(' ')
                    if valor1 == 'x':
                        x = x + int(valor2)
                    elif valor1 == 'y':
                        y = y + int(valor2)
                # soma os valores para simular uma soma de valores negativos
                if linha.startswith('$v'):
                    if ativacao_if == True:
                        operacao, valor1, valor2 = linha.split(' ')
                        if valor1 == 'x':
                            x = x + int(valor2)
                        elif valor1 == 'y':
                            y = y + int(valor2)
                if linha.startswith('cs'):
                    caso = linha.split(' ')
                    if caso[1] == 'y':
                        ativacao_if = trata_condicionais(y, caso[2], int(caso[3]))
                    elif caso[1] == 'x':
                        ativacao_if = trata_condicionais(x, caso[2], int(caso[3]))
                # inseri um valor para pr
                if linha.startswith('$pr=') or linha.startswith('$pr ='):
                    if ativacao_if == True:
                        if procura_caractere(linha, '=', 'p'):
                            pixel_retorna = pixel
                        else:
                            if linha[linha.find('=')] != linha[-1]:
                                vereficacao = procura_dados(linha[linha.find('=') + 1:], estruturas_dados)
                                if vereficacao == None:
                                    if linha[linha.find('=') + 1] == ' ':
                                        pixel_retorna = linha[linha.find('=') + 2]
                                    else:
                                        pixel_retorna = linha[linha.find('=') + 1]
                                elif vereficacao != None:
                                    pixel_retorna = vereficacao
                # inseri um valor para cp
                if linha.startswith('$cp=') or linha.startswith('$cp ='):
                    if ativacao_if == True:
                        vereficacao = procura_dados(linha[linha.find('=') + 1:], estruturas_dados)
                        if linha[linha.find('=')] != linha[-1] and vereficacao == None:
                            cor_pixel = linha[linha.find('=') + 1:]
                        elif vereficacao != None:
                            cor_pixel = vereficacao
                # acaba com condicional
                if linha.startswith('ec'):
                    if ativacao_if == True:
                        ativacao_if = False
                # cria variável
                if linha.startswith('l'):
                    inicio, final = linha.split('=')
                    inicio = inicio[1:].strip()
                    final = final.strip()
                    vereficacao = procura_dados(inicio, estruturas_dados)
                    if vereficacao == None and inicio != 'p':
                        estruturas_dados['variáveis'].append([inicio, final])
                # cria variável
                if linha.startswith('$l'):
                    if ativacao_if == True:
                        inicio, final = linha.split('=')
                        inicio = inicio[1:].strip()
                        final = final.strip()
                        vereficacao = procura_dados(inicio, estruturas_dados)
                        if vereficacao == None:
                            estruturas_dados['variáveis'].append([inicio, final])
                # cria vetor
                if linha.startswith('t'):
                    dados = linha.split(' ')
                    if dados[1] != 'p':
                        # verefica se existe outro vetor com outro nome
                        achou = False
                        for v in estruturas_dados['vetores']:
                            if v[0] == dados[1]:
                                achou = True
                        if achou == False:
                            estruturas_dados['vetores'].append([dados[1], dados[2:]])
                # inseri valor de um vetor nas posições de saída(por isso ot de out, que é saída em inglês)
                if linha.startswith('ot'):
                    dados = linha.split(' ')
                    if 'x' in dados[1] and 'y' in dados[1]:
                        for v in estruturas_dados['vetores']:
                            if v[0] == dados[2]:
                                if int(v[1][0]) <= largura_tela and int(v[1][1]) <= altura_tela:
                                    x = int(v[1][0])
                                    y = int(v[1][1])
                                    break
                # soma um valor(causando soma negativa visualmente) de um vetor nas posições de saída(por isso ot de out, que é saída em inglês)
                if linha.startswith('ts'):
                    dados = linha.split(' ')
                    if 'x' in dados[1] and 'y' in dados[1]:
                        for v in estruturas_dados['vetores']:
                            if v[0] == dados[2]:
                                if int(v[1][0]) + x <= largura_tela and int(v[1][1]) + y <= altura_tela:
                                    x += int(v[1][0])
                                    y += int(v[1][1])
                                    break
                # soma um valor(causando soma positiva visualmente) de um vetor nas posições de saída(por isso ot de out, que é saída em inglês)
                if linha.startswith('tp'):
                    dados = linha.split(' ')
                    if 'x' in dados[1] and 'y' in dados[1]:
                        for v in estruturas_dados['vetores']:
                            if v[0] == dados[2]:
                                x -= int(v[1][0])
                                y -= int(v[1][1])
                                break
                # inseri valor de um vetor nas posições de saída(por isso ot de out, que é saída em inglês)
                if linha.startswith('$ot'):
                    if ativacao_if == True:
                        dados = linha.split(' ')
                        if 'x' in dados[1] and 'y' in dados[1]:
                            for v in estruturas_dados['vetores']:
                                if v[0] == dados[2]:
                                    if int(v[1][0]) <= largura_tela and int(v[1][1]) <= altura_tela:
                                        x = int(v[1][0])
                                        y = int(v[1][1])
                                        break
                # soma um valor(causando soma negativa visualmente) de um vetor nas posições de saída(por isso ot de out, que é saída em inglês)
                if linha.startswith('$ts'):
                    if ativacao_if == True:
                        dados = linha.split(' ')
                        if 'x' in dados[1] and 'y' in dados[1]:
                            for v in estruturas_dados['vetores']:
                                if v[0] == dados[2]:
                                    if int(v[1][0]) + x <= largura_tela and int(v[1][1]) + y <= altura_tela:
                                        x += int(v[1][0])
                                        y += int(v[1][1])
                                        break
                # soma um valor(causando soma positiva visualmente) de um vetor nas posições de saída(por isso ot de out, que é saída em inglês)
                if linha.startswith('$tp'):
                    if ativacao_if == True:
                        dados = linha.split(' ')
                        if 'x' in dados[1] and 'y' in dados[1]:
                            for v in estruturas_dados['vetores']:
                                if v[0] == dados[2]:
                                    x -= int(v[1][0])
                                    y -= int(v[1][1])
                                    break
                # faz uma operação matemática a algum valor com o cosseno de um ângulo
                if linha.startswith('COS'):
                    funcao, valor , operacao ,  angulo = linha.split(' ')
                    if operacao == '+':
                        if valor == 'x':
                            if int(x + math.cos(math.radians(int(angulo)))) < largura_tela:
                                x += math.cos(math.radians(int(angulo)))
                        elif valor == 'y':
                            if int(y + math.cos(math.radians(int(angulo)))) < altura_tela:
                                y += math.cos(math.radians(int(angulo)))
                    elif operacao == '-':
                        if valor == 'x':
                            if int(x - math.cos(math.radians(int(angulo)))) > 0:
                                x -= math.cos(math.radians(int(angulo)))
                        elif valor == 'y':
                            if int(y - math.cos(math.radians(int(angulo)))) > 0:
                                y -= math.cos(math.radians(int(angulo)))
                    elif operacao == '*':
                        if valor == 'x':
                            if int(x * math.cos(math.radians(int(angulo)))) < largura_tela:
                                x *= math.cos(math.radians(int(angulo)))
                        elif valor == 'y':
                            if int(y * math.cos(math.radians(int(angulo)))) < altura_tela:
                                y *= math.cos(math.radians(int(angulo)))
                # faz uma operação matemática a algum valor com o seno de um ângulo
                if linha.startswith('SIN'):
                    funcao, valor, operacao, angulo = linha.split(' ')
                    if operacao == '+':
                        if valor == 'x':
                            if int(x + math.sin(math.radians(int(angulo)))) < largura_tela:
                                x += math.sin(math.radians(int(angulo)))
                        elif valor == 'y':
                            if int(y + math.sin(math.radians(int(angulo)))) < altura_tela:
                                y += math.sin(math.radians(int(angulo)))
                    elif operacao == '-':
                        if valor == 'x':
                            if int(x - math.sin(math.radians(int(angulo)))) > 0:
                                x -= math.sin(math.radians(int(angulo)))
                        elif valor == 'y':
                            if int(y - math.sin(math.radians(int(angulo)))) > 0:
                                y -= math.sin(math.radians(int(angulo)))
                    elif operacao == '*':
                        if valor == 'x':
                            if int(x * math.sin(math.radians(int(angulo)))) < largura_tela:
                                x *= math.sin(math.radians(int(angulo)))
                        elif valor == 'y':
                            if int(y * math.sin(math.radians(int(angulo)))) < altura_tela:
                                y *= math.sin(math.radians(int(angulo)))
                # faz uma operação matemática a algum valor com o cosseno de um ângulo
                if linha.startswith('$COS'):
                    if ativacao_if == True:
                        funcao, valor, operacao, angulo = linha.split(' ')
                        if operacao == '+':
                            if valor == 'x':
                                if int(x + math.cos(math.radians(int(angulo)))) < largura_tela:
                                    x += math.cos(math.radians(int(angulo)))
                            elif valor == 'y':
                                if int(y + math.cos(math.radians(int(angulo)))) < altura_tela:
                                    y += math.cos(math.radians(int(angulo)))
                        elif operacao == '-':
                            if valor == 'x':
                                if int(x - math.cos(math.radians(int(angulo)))) > 0:
                                    x -= math.cos(math.radians(int(angulo)))
                            elif valor == 'y':
                                if int(y - math.cos(math.radians(int(angulo)))) > 0:
                                    y -= math.cos(math.radians(int(angulo)))
                        elif operacao == '*':
                            if valor == 'x':
                                if int(x * math.cos(math.radians(int(angulo)))) < largura_tela:
                                    x *= math.cos(math.radians(int(angulo)))
                            elif valor == 'y':
                                if int(y * math.cos(math.radians(int(angulo)))) < altura_tela:
                                    y *= math.cos(math.radians(int(angulo)))
                # faz uma operação matemática a algum valor com o seno de um ângulo
                if linha.startswith('$SIN'):
                    if ativacao_if == True:
                        funcao, valor, operacao, angulo = linha.split(' ')
                        if operacao == '+':
                            if valor == 'x':
                                if int(x + math.sin(math.radians(int(angulo)))) < largura_tela:
                                    x += math.sin(math.radians(int(angulo)))
                            elif valor == 'y':
                                if int(y + math.sin(math.radians(int(angulo)))) < altura_tela:
                                    y += math.sin(math.radians(int(angulo)))
                        elif operacao == '-':
                            if valor == 'x':
                                if int(x - math.sin(math.radians(int(angulo)))) > 0:
                                    x -= math.sin(math.radians(int(angulo)))
                            elif valor == 'y':
                                if int(y - math.sin(math.radians(int(angulo)))) > 0:
                                    y -= math.sin(math.radians(int(angulo)))
                        elif operacao == '*':
                            if valor == 'x':
                                if int(x * math.sin(math.radians(int(angulo)))) < largura_tela:
                                    x *= math.sin(math.radians(int(angulo)))
                            elif valor == 'y':
                                if int(y * math.sin(math.radians(int(angulo)))) < altura_tela:
                                    y *= math.sin(math.radians(int(angulo)))
                # faz uma multiplicação entre vetor e matriz
                if linha.startswith('MMV'):
                    # sintaxe: comando índice vetor
                    comando, indice , vetor = linha.split(' ')
                    if len(buffer_de_matrizes) > 0:
                        if vetor == 'xy':
                            vetor_resultado = multiplicacao_matricial(buffer_de_matrizes[f'{indice}'],[x,y])
                            if len(vetor_resultado) > 0:
                                if vetor_resultado[0] < largura_tela and vetor_resultado[1] < altura_tela:
                                    x = vetor_resultado[0]
                                    y = vetor_resultado[1]
                        else:
                            for pos,v in enumerate(estruturas_dados['vetores']):
                                if v[0] == vetor:
                                    vetor_resultado = multiplicacao_matricial(buffer_de_matrizes[f'{indice}'],v[1])
                                    estruturas_dados['vetores'][pos][1] = vetor_resultado
                # faz uma multiplicação entre vetor e matriz
                if linha.startswith('$MMV'):
                    if ativacao_if == True:
                        # sintaxe: comando índice vetor
                        comando, indice, vetor = linha.split(' ')
                        if len(buffer_de_matrizes) > 0:
                            if vetor == 'xy':
                                vetor_resultado = multiplicacao_matricial(buffer_de_matrizes[f'{indice}'], [x, y])
                                if len(vetor_resultado) > 0:
                                    if vetor_resultado[0] < largura_tela and vetor_resultado[1] < altura_tela:
                                        x = vetor_resultado[0]
                                        y = vetor_resultado[1]
                            else:
                                for pos, v in enumerate(estruturas_dados['vetores']):
                                    if v[0] == vetor:
                                        vetor_resultado = multiplicacao_matricial(buffer_de_matrizes[f'{indice}'], v[1])
                                        estruturas_dados['vetores'][pos][1] = vetor_resultado
                # faz uma operação matemática a algum valor com o tangente de um ângulo
                if linha.startswith('TAN'):
                    funcao, valor, operacao, angulo = linha.split(' ')
                    if operacao == '+':
                        if valor == 'x':
                            if int(x + math.tan(math.radians(int(angulo)))) < largura_tela:
                                x += math.tan(math.radians(int(angulo)))
                        elif valor == 'y':
                            if int(y + math.tan(math.radians(int(angulo)))) < altura_tela:
                                y += math.tan(math.radians(int(angulo)))
                    elif operacao == '-':
                        if valor == 'x':
                            if int(x - math.tan(math.radians(int(angulo)))) > 0:
                                x -= math.tan(math.radians(int(angulo)))
                        elif valor == 'y':
                            if int(y - math.tan(math.radians(int(angulo)))) > 0:
                                y -= math.tan(math.radians(int(angulo)))
                    elif operacao == '*':
                        if valor == 'x':
                            if int(x * math.tan(math.radians(int(angulo)))) < largura_tela:
                                x *= math.cos(math.radians(int(angulo)))
                        elif valor == 'y':
                            if int(y * math.tan(math.radians(int(angulo)))) < altura_tela:
                                y *= math.cos(math.radians(int(angulo)))
                # faz uma operação matemática a algum valor com o tangente de um ângulo
                if linha.startswith('$TAN'):
                    if ativacao_if == True:
                        funcao, valor, operacao, angulo = linha.split(' ')
                        if operacao == '+':
                            if valor == 'x':
                                if int(x + math.tan(math.radians(int(angulo)))) < largura_tela:
                                    x += math.tan(math.radians(int(angulo)))
                            elif valor == 'y':
                                if int(y + math.tan(math.radians(int(angulo)))) < altura_tela:
                                    y += math.tan(math.radians(int(angulo)))
                        elif operacao == '-':
                            if valor == 'x':
                                if int(x - math.tan(math.radians(int(angulo)))) > 0:
                                    x -= math.tan(math.radians(int(angulo)))
                            elif valor == 'y':
                                if int(y - math.tan(math.radians(int(angulo)))) > 0:
                                    y -= math.tan(math.radians(int(angulo)))
                        elif operacao == '*':
                            if valor == 'x':
                                if int(x * math.tan(math.radians(int(angulo)))) < largura_tela:
                                    x *= math.cos(math.radians(int(angulo)))
                            elif valor == 'y':
                                if int(y * math.tan(math.radians(int(angulo)))) < altura_tela:
                                    y *= math.cos(math.radians(int(angulo)))
                # função que faz um valor receber ele ao quadrado
                if linha.startswith('PW2'):
                    comando , numero = linha.split(' ')
                    if numero == 'x':
                        if x**2 < largura_tela:
                            x = x**2
                    elif numero == 'y':
                        if y**2 < altura_tela:
                            y = y**2
                    else:
                        valor = procura_dados(numero,estruturas_dados)
                        for pos,v in enumerate(estruturas_dados['variáveis']):
                            if v[0] == numero:
                                estruturas_dados['variáveis'][pos][1] = int(valor)**2
                # função que faz um valor receber ele ao cubo
                if linha.startswith('PW3'):
                    comando , numero = linha.split(' ')
                    if numero == 'x':
                        if x**3 < largura_tela:
                            x = x**3
                    elif numero == 'y':
                        if y**3 < altura_tela:
                            y = y**3
                    else:
                        valor = procura_dados(numero,estruturas_dados)
                        for pos,v in enumerate(estruturas_dados['variáveis']):
                            if v[0] == numero:
                                estruturas_dados['variáveis'][pos][1] = int(valor)**3
                linha = ''
    return [f'\033[{cor_pixel}m{pixel_retorna}\033[m', int(x), int(y)]
# função para utilização do código LSLN(linguagem de sombreamento da libraryRenderNatan)
def utiliza_codigo_LSLN(codigo):
    global tela
    for pos0, c in enumerate(tela):
        for pos1, p in enumerate(c):
            if p != ' ':
                tela[pos0][pos1] = ' '
                pixel = compila_codigo_LSLN(codigo, p, pos1, pos0)
                if pixel[2] > 0 and pixel[1] > 0:
                    tela[pixel[2]][pixel[1]] = pixel[0]
###############################################################
#                    FUNÇÕES DE LIMPEZA
###############################################################
# limpa a tela
def limpa_tela():
    global tela
    for pos0, c in enumerate(tela):
        for pos1, v in enumerate(c):
            if v != ' ':
                tela[pos0][pos1] = ' '
# limpa o z-buffer
def limpa_z_buffer():
    global z_buffer
    z_buffer = []
# trata o terminal, e o fps
def trata_terminal(fps):
    # trata fps
    if fps == 1:
        time.sleep(0.032)
    elif fps == 2:
        time.sleep(0.016)
    elif fps == 3:
        time.sleep(0.008)
    elif fps == 4:
        time.sleep(0.004)
    elif fps == 5:
        time.sleep(0.002)
    elif fps == 6:
        time.sleep(0.001)
    # limpa terminal
    sys.stdout.write("\033[H")
    sys.stdout.flush()
    # some o cursor de digitação
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()
###############################################################
#                   FUNÇÕES UTILITÁRIAS
###############################################################
def converte_RGB_ANSI(cores):
    cores_ANSI = []
    for cor in cores:
        if cor == [1,0,0]:
            cores_ANSI.append(31)
        elif cor == [0,1,0]:
            cores_ANSI.append(32)
        elif cor == [0,0,1]:
            cores_ANSI.append(34)
        elif cor == [1,1,0]:
            cores_ANSI.append(33)
        elif cor == [0,1,1]:
            cores_ANSI.append(36)
        elif cor == [1,0,1]:
            cores_ANSI.append(35)
        elif cor == [0,0,0]:
            cores_ANSI.append(30)
        elif cor == [1,1,1]:
            cores_ANSI.append(37)
    return cores_ANSI
###############################################################
#                 FUNÇÕES DE RENDERIZAÇÃO
###############################################################
# função para z-buffer
def valida_z_buffer(x, y, z):
    global z_buffer
    achou = True
    for pos, v in enumerate(z_buffer):
        if v[0] == x and v[1] == y and v[2] < z:
            achou = False
    return achou
# função para adicionar dados a um dos buffers
def adiciona_dados(tipo_de_buffer, dados, indice=0):
    global buffer_de_vertices, buffer_de_aparencia
    # parte para tratamento dos dados do BDV
    if tipo_de_buffer == 'BDV':
        if len(dados) > 0:
            buffer_de_vertices = dados
        else:
            print('\033[31mErro:Não há suporte para os dados que seriam adicionados\033[m')
    # parte para tratamento dos dados do BDA
    elif tipo_de_buffer == 'BDA':
        if len(dados) > 0:
            buffer_de_aparencia = dados
        else:
            print('\033[31mErro:Não há nenhum dado para adicionar\033[m')
    # parte para tratamento de dados do BDM
    elif tipo_de_buffer == 'BDM':
        if indice != 0:
            buffer_de_matrizes[f'{indice}'] = dados
    else:
        print('\033[31mErro:Não existe buffer com o nome informado\033[m')
# função para criar uma tela para o desenho
def cria_tela(altura,largura):
    global tela,altura_tela,largura_tela,z_buffer
    altura_tela = altura
    largura_tela = largura
    # cria tela com base na altura e largura da tela
    for c in range(0,altura_tela):
        tela.append([])
        for v in range(0,largura_tela):
            tela[c].append(' ')
# função para projeção dos vértices
def projeta_vertices():
    global tela,buffer_de_vertices,buffer_de_aparencia,altura_tela,largura_tela
    # retira o que havia antes na tela
    limpa_tela()
    # retira o que havia antes no z-buffer
    limpa_z_buffer()
    # buffer com os vértices projetados
    buffer_projetado = []
    # faz um loop que cálcula cada vértice para ser projetado
    for pos0,c in enumerate(buffer_de_vertices):
        if c[2] > 0:
            # (x/z) + (x_tela/2)
            x = (c[0]/c[2]) + (largura_tela/2)
            # (y/z) + (y_tela/2)
            y = (c[1]/c[2]) + (altura_tela/2)
            # desenha
            if int(y) < altura_tela and int(x) < largura_tela:
                if pos0 < len(buffer_de_aparencia):
                    buffer_projetado.append([int(x),int(y),c[2],True])
                else:
                    buffer_projetado.append([int(x), int(y),c[2], False])
    return buffer_projetado
# função para desenho de linhas
def desenha_linhas(buffer_projetado,comeco,termino,cor=0):
    global tela
    buffer_pixel_linha = []
    if termino % 2 == 0:
        conjunto_1 = []
        conjunto_2 = []
        # obtenção dos vértices
        for pos0,c in enumerate(buffer_projetado[comeco:termino]):
            if pos0 % 2 == 0:
                conjunto_1.append(c)
            elif pos0 % 2 != 0:
                conjunto_2.append(c)
        # cálculos para desenho das linhas
        for pos1, v in enumerate(conjunto_1):
            delta_x = abs(conjunto_2[pos1][0]-v[0])
            delta_y = abs(conjunto_2[pos1][1]-v[1])
            # verifica o passo que deve ser feito em x e y
            passo_x = 0
            if v[0] < conjunto_2[pos1][0]:
                passo_x = 1
            else:
                passo_x = -1

            passo_y = 0
            if v[1] < conjunto_2[pos1][1]:
                passo_y = 1
            else:
                passo_y = -1

            # nomeia de forma mais legível
            x = v[0]
            y = v[1]

            if delta_x > delta_y:
                p = 2 * delta_y - delta_x
                while x != conjunto_2[pos1][0]:
                    valida = valida_z_buffer(x, y, v[2])
                    if valida == True:
                        tela[y][x] = f'\033[{cor}m.\033[m'
                        z_buffer.append([x,y, v[2]])
                    buffer_pixel_linha.append([x,y,v[2]])
                    if p >= 0:
                        y += passo_y
                        p += 2 * (delta_y-delta_x)
                    else:
                        p += 2 * delta_y
                    x += passo_x
            else:
                p = 2 * delta_y - delta_x
                while y != conjunto_2[pos1][1]:
                    valida = valida_z_buffer(x, y, v[2])
                    if valida == True:
                        tela[y][x] = f'\033[{cor}m.\033[m'
                        z_buffer.append([x, y, v[2]])
                    buffer_pixel_linha.append([x, y,v[2]])
                    if p >= 0:
                        x += passo_x
                    else:
                        p += 2 * delta_x
                    y += passo_y
    return buffer_pixel_linha
# função para desenho de pontos
def desenha_pontos(buffer_projetado):
    global tela,altura_tela,largura_tela,z_buffer
    for pos0,c in enumerate(buffer_projetado):
        if c[3] == True:
            if c[1] > 0 and c[1] < altura_tela:
                if c[0] > 0 and c[0] < largura_tela:
                    valida = valida_z_buffer(c[0], c[1], c[2])
                    if valida == True:
                        tela[c[1]][c[0]] = f'\033[{buffer_de_aparencia[pos0]}m.\033[m'
                        z_buffer.append([c[0],c[1],c[2]])
        else:
            if c[1] > 0 and c[1] < altura_tela:
                if c[0] > 0 and c[0] < largura_tela:
                    valida = valida_z_buffer(c[0], c[1], c[2])
                    if valida == True:
                        tela[c[1]][c[0]] = f'.'
                        z_buffer.append([c[0],c[1],c[2]])
    return tela
# função para preenchimento de forma
def preenche_forma(buffer_pontos_linhas,cores):
    global tela,altura_tela,largura_tela
    cor1 = cores[0]
    cor2 = cores[1]
    if buffer_pontos_linhas:
        # esqueci do que faz exatamente
        lista_x = []
        lista_y = []
        for pos0,c in enumerate(buffer_pontos_linhas):
            lista_x.append(c[0])
            lista_y.append(c[1])

            menor_x = int(max(0, min(lista_x)))
            maior_x = int(min(largura_tela - 1, max(lista_x)))
            menor_y = int(max(0, min(lista_y)))
            maior_y = int(min(altura_tela - 1, max(lista_y)))

            linhas_x = {}
            for v in range(menor_y,maior_y+1):
                linhas_x[v] = []
            for p in buffer_pontos_linhas:
                ponto_x, ponto_y = int(p[0]), int(p[1])
                if menor_y <= ponto_y <= maior_y:
                    linhas_x[ponto_y].append(ponto_x)

            # seleciona as coordenadas que estão dentro da forma
            testurizacao = True
            for y in range(menor_y,maior_y+1):
                x_inicio = max(menor_x,min(linhas_x[y]))
                x_fim = min(maior_x,max(linhas_x[y]))
                # trata textura
                if testurizacao == True:
                    testurizacao = False
                elif testurizacao == False:
                    testurizacao = True
                for x in range(x_inicio,x_fim+1):
                    z_atual = buffer_pontos_linhas[0][2]
                    # trata textura
                    valida = valida_z_buffer(x, y, z_atual)
                    if valida == True:
                        if testurizacao == True:
                            tela[y][x] = f'\033[{cor1}m.\033[m'
                        elif testurizacao == False:
                            tela[y][x] = f'\033[{cor2}m.\033[m'
                        z_buffer.append([x,y,z_atual])

                    if testurizacao == True:
                        testurizacao = False
                    elif testurizacao == False:
                        testurizacao = True

                    valida = valida_z_buffer(x, y, z_atual)
                    if valida == True:
                        if testurizacao == True:
                            tela[y][x] = f'\033[{cor1}m.\033[m'
                        elif testurizacao == False:
                            tela[y][x] = f'\033[{cor2}m.\033[m'
                        z_buffer.append([x, y, z_atual])
# função para desenho da tela
def desenha_tela(tela_recebida):
    for c in tela_recebida:
        for v in c:
            # print(v,end=' ')
            sys.stdout.write(f'{v} ')
        # print()
        sys.stdout.write('\n')