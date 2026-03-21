import os
mapa = [[2, 0, 1],
        [2, 0, 2],
        [2, 0, 0]]


# Mostrar mapa inicial
def desenhar():
    for linha in mapa:
        print(linha)


desenhar()

while True:
    escolha = input("Deseja se mover para onde (999 para parar)? (linha coluna): ")
    if escolha == '999':
        break
    partes = escolha.split()
    # Converter entrada para inteiros
    nova_linha = int(partes[0])
    nova_coluna = int(partes[1])
    # Encontrar posição atual do jogador
    achou = False
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == 1:
                linha_atual, coluna_atual = i, j
                achou = True
                break
        if achou:
            break

    # Apagar posição antiga
    if mapa[nova_linha][nova_coluna] == 0:
        mapa[linha_atual][coluna_atual] = 0
        mapa[nova_linha][nova_coluna] = 1
    else:
        print('a uma parede nessa posição')

    os.system('cls')
    desenhar()
