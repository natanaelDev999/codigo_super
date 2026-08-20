tela = []


def cria_tela(altura, largura):
    global tela
    tamanho = altura * largura
    tamanho = tamanho - (tamanho % largura)
    for c in range(0, tamanho):
        tela.append(0)


def desenha_tela(largura):
    global tela
    for pos0, c in enumerate(tela):
        if pos0 % largura != 0:
            print(c, end=' ')
        else:
            print()


def desenha_ponto(xy, altura, largura):
    global tela

    xy[1] += int(altura / 2)
    xy[0] += int(largura / 2)

    cY = 0
    cX = 0

    for pos0, c in enumerate(tela):
        if cY == xy[1] and cX == xy[0]:
            tela[pos0] = 1
        if pos0 % largura == 0:
            cY += 1
            cX = 0
        else:
            cX += 1


def main():
    altura = 8
    largura = 9
    cria_tela(altura, largura)
    desenha_ponto([-4, 0], altura, largura)
    desenha_tela(largura)


main()