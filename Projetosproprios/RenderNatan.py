# buffer de desenho
# estrutura de dados: [x,y,z,color(se haverá cor)]
# -y cima, y baixo, o mesmo acontece com outras coordenadas
buffer_de_desenho = [[0,0,2,True]]
# buffer de aparência
# estrutura de dados: número(\033[ número m \033[m)
buffer_de_aparencia = [31]
# variáveis para projeção
w = 16
h = 10
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
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],]
# função para obter as coordenadas do objeto na tela
def coordenadas_transformadas():
    global buffer_de_desenho, w, h
    buffer_de_desenho_transformado = []
    for c in buffer_de_desenho:
        buffer_de_desenho_transformado.append([((c[0])/c[2]) + (w/2),
                                               ((c[1]) / c[2]) + (h/2),c[3]])
    return buffer_de_desenho_transformado

# função para linha
def linha(tipo,quant):
    if tipo == 1:
        print(quant*'-')
    elif tipo == 2:
        print(quant*'-=')
# função para atualização de tela
def atualiza_tela(buffer_transformado):
    global tela,buffer_de_aparencia
    for pos,c in enumerate(buffer_transformado):
        print(c)
        print(buffer_de_aparencia[pos])
        if int(c[1]-1) < 9 and int(c[0]-1) < 15 and c[2] == True:
            tela[int(c[1])-1][int(c[0])-1] = f'\033[{buffer_de_aparencia[pos]}m.\033[m'
        if int(c[1]-1) < 9 and int(c[0]-1) < 15 and c[2] == False:
            tela[int(c[1])-1][int(c[0])-1] = '.'

# função de desenho
def desenho_tela():
    global tela
    linha(2,16)
    for c in tela:
        for v in c:
            print(v,end=' ')
        print()
    linha(2,16)
# função principal, onde tudo acontece
def main():
    atualiza_tela(coordenadas_transformadas())
    desenho_tela()
main()