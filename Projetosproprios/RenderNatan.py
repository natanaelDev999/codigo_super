# biblioteca para controle do fps
from time import sleep
# biblioteca para limpar o terminal
import sys
# biblioteca para manter o buffer_de_desenho_original
from copy import deepcopy
# variáveis para o programa
# valores para camera
# estrutura de dados: [x, y, z]
coordenadas_camera = [0,0,0]
# buffer de desenho
# estrutura de dados: [x,y,z,cor(se haverá cor)]
# -y cima, y baixo, o mesmo acontece com outras coordenadas
buffer_de_desenho = [[-4,4,1,True],
                     [4,4,1,True],
                     [4,4,1,True],
                     [0,0,1,True],
                     [0,0,1,True],
                     [-4,4,1,True]]
# buffer de preservação de coordenadas originais
buffer_de_desenho_original = []
# buffer de aparência
# estrutura de dados: número(\033[ número m \033[m)
buffer_de_aparencia = [34,34,34,34,34,34]
# buffer de aparência para linhas
# estrutura de dados: número(\033[ número m \033[m)
buffer_de_aparencia_linha = [31]
# buffer para posição dos pixels das linhas
buffer_posicao_pixel = []
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
# função para estilização com linha
def linha_estilizacao():
    print(30*'-')
# estados do renderizador
def estado_render():
    global buffer_de_desenho,coordenadas_camera,buffer_de_aparencia,buffer_de_aparencia_linha
    linha_estilizacao()
    print('\033[36m ESTADOS DO RENDERIZADOR RENDERNATAN\033[m')
    print(f'\033[33mQuantidade de vértices no buffer_de_desenho\033[m: {len(buffer_de_desenho)}')
    print(f'\033[31mQuantidade de sub-shaders no buffer_de_aparencia\033[m: {len(buffer_de_aparencia)}')
    print(f'\033[34mQuantidade de valores de cor para as linha:\033[m: {len(buffer_de_aparencia_linha)}')
    print(f'\033[36mPosição da câmera\033[m: x:{coordenadas_camera[0]}; y:{coordenadas_camera[1]}; z:{coordenadas_camera[2]}')
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
    global coordenadas_camera,buffer_de_desenho,buffer_de_desenho_original
    buffer_de_desenho_original = deepcopy(buffer_de_desenho)
    for cod in buffer_de_desenho:
        if coordenadas_camera[0] <= 4 and coordenadas_camera[1] <= 5 and coordenadas_camera[2] <= 5:
            cod[0] -= coordenadas_camera[0]
            cod[1] -= coordenadas_camera[1]
            cod[2] += coordenadas_camera[2]
# função para obter as coordenadas do objeto na tela
def coordenadas_transformadas():
    global buffer_de_desenho, w, h
    buffer_de_desenho_transformado = []
    for c in buffer_de_desenho:
        # estrutura de dado: [x_tela , y_tela , cor , z(para z-buffer)]
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
            if int(c[1]) < h and int(c[0]) < w and c[2] == True:
                tela[int(c[1])][int(c[0])] = f'\033[{buffer_de_aparencia[pos]}m.\033[m'
            if int(c[1]) < h and int(c[0]) < w and c[2] == False:
                tela[int(c[1])][int(c[0])] = '.'
            z_buffer.append([c[0],c[1],c[3]])
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
    for pos,v in enumerate(ponto1):
        dx = abs(ponto2[pos][0]-v[0])
        dy = abs(ponto2[pos][1]-v[1])
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
            p = 2*dy-dx
            while x != ponto2[pos][0]:
                if y < h and x < w:
                    achou = z_buffer_atualizacao(x,y,v[3])
                    if achou == False:
                        if cor == False:
                            tela[int(y)][int(x)] = '.'
                        else:
                            tela[int(y)][int(x)] = f'\033[{buffer_de_aparencia_linha[pos_cor]}m.\033[m'
                        z_buffer.append([x,y,v[3]])
                        buffer_posicao_pixel.append([x,y])
                if p >= 0:
                    y += passo_y
                    p += 2 * (dy-dx)
                else:
                    p += 2 * dy
                x += passo_x
        else:
            p = 2 * dx - dy
            while y != ponto2[pos][1]:
                if y < h and x < w:
                    achou = z_buffer_atualizacao(x, y, v[3])
                    if achou == False:
                        if cor == False:
                            tela[int(y)][int(x)] = '.'
                        else:
                            tela[int(y)][int(x)] = f'\033[{buffer_de_aparencia_linha[pos_cor]}m.\033[m'
                        z_buffer.append([x, y, v[3]])
                        buffer_posicao_pixel.append([x,y])
                if p >= 0:
                    x += passo_x
                else:
                    p += 2 * dx
                y += passo_y
def y_maior():
    global buffer_posicao_pixel
    maior = buffer_posicao_pixel[0][1]
    for c in buffer_posicao_pixel:
        if c[1] > maior:
            maior = c[1]
    return maior
# função para preencher as formas
def preenche_forma(cor,começo,termino):
    global buffer_de_desenho,buffer_posicao_pixel,h,w,tela
    if len(buffer_de_desenho) >= 3:
        # valor para limite
        maior = y_maior()
        # rodar todo o buffer para as posições dos pixeis
        for px in buffer_posicao_pixel[começo:termino]:
            # contador para terminar o loop e marcar base do objeto
            cont = 1
            # loop para desenhar '#' até a base do objeto
            while cont < maior and px[1]+cont < h and px[0] < w and int(px[1]+cont) <= maior:
                tela[int(px[1]+cont)][int(px[0])] = f'\033[{cor}m#\033[m'
                cont += 1
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
    global tela,buffer_de_desenho_original,buffer_de_desenho
    linha(2,16)
    for c in tela:
        for v in c:
            print(v,end=' ')
        print()
    linha(2,16)
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
# função principal, onde tudo acontece
def main():
    global buffer_de_desenho,coordenadas_camera
    # mostra estado
    estado_render()
    sleep(4)
    while True:
        # pineple => transforma as coordenas em relação a camera => carrega o buffer de desenho => utiliza o buffer de desenho para
        # desenhar os vértices => utiliza o buffer de desenho com base para conectar linhas => utiliza as coordenadas das linhas
        # para preencher formas => utiliza o shader de fundo para pintar o fundo => limpa os buffers de tela e das linhas => limpa a
        # tela e controla o fps
        # modifica e utiliza os buffers
        coordenadas_camera_transformadas()
        buffer = coordenadas_transformadas()
        atualiza_tela_pontos(buffer)
        atualiza_tela_linhas(buffer,6,0,0,True)
        preenche_forma(33,0,20)
        pintar_fundo_shader()
        desenho_tela()
        limpa_pixels_linhas_buffer()
        limpa_tela_buffer()
        #
        # controla o fps
        sleep(0.5)
        # limpa terminal
        sys.stdout.write("\033c")
        sys.stdout.flush()
        # some o cursor de digitação
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()
main()