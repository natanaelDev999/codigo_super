import LibraryVectorNatan as lvn


tela = []
buffer = []


def cria_tela(altura, largura):
    global tela
    tamanho = altura * largura
    tamanho = tamanho - (tamanho % largura)
    for c in range(0, tamanho):
        tela.append('\033[0;0;45m \033[m')


def desenha_tela(largura):
    global tela
    for pos0, c in enumerate(tela):
        if pos0 % largura != 0:
            print(c, end='')
        else:
            print()


def cria_ponto(xy, altura, largura):
    global tela,buffer

    if xy[2] != 0:

        xy[1] = (xy[1]/xy[2])+int(altura / 2)
        xy[0] = (xy[0]/xy[2])+int(largura / 2)

        cY = 0
        cX = 0

        for pos0, c in enumerate(tela):
            if cY == xy[1] and cX == xy[0]:
                buffer.append(pos0)
            if pos0 % largura == 0:
                cY += 1
                cX = 0
            else:
                cX += 1

def perpendicular(vetor):
    return [vetor[1],-vetor[0]]

def ponto_teste_dentro(a,b,p):
    ap = [p[0] - a[0],p[1]-a[1]]
    abPerp = perpendicular([b[0]-a[0],b[1]-a[1]])
    return lvn.produto_escalar(ap,abPerp) >= 0

def ponto_triangulo(a,b,c,p):
    sideAB = ponto_teste_dentro(a,b,p)

    sideBC = ponto_teste_dentro(b,c,p)

    sideCA = ponto_teste_dentro(c,a,p)

    return sideAB == sideBC and sideBC == sideCA


def cria_triangulo(a,b,c,largura,altura):
    cY = 0
    cX = 0


    a = [a[0]+(largura/2),a[1]+(altura/2)]
    b = [b[0]+(largura/2),b[1]+(altura/2)]
    c = [c[0]+(largura/2),c[1]+(altura/2)]


    for pos0,i in enumerate(tela):
        if pos0 % largura == 0:
            cY += 1
            cX = 0
        else:
            cX += 1
        if ponto_triangulo(a,b,c,[cX,cY]) == True:
            buffer.append(pos0)


def desenha_buffer():
    global buffer
    for c in buffer:
        tela[c] = '\033[33m█\033[m'


def main():
    altura = 35
    largura = 100
    cria_tela(altura, largura)
    # cria_triangulo([0,0],[-8,8],[8,8],largura,altura)
    cria_ponto([0,0,1],altura,largura)
    desenha_buffer()
    desenha_tela(largura)


main()