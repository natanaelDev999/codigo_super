#              RAY TRACING
#criado em: 26/8/2026
#----------------------------------------
import LibraryVectorNatan as lvn
# variáveis principais
vetor_pos = [0, 0, 0]
vetor_dir = [0, 0, 1]
matriz_mun = [[
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
],

    [
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],

    [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]]
matriz_vis = [[' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ']]
def RayTracing():
    global vetor_pos,vetor_dir,matriz_mun,matriz_vis
    for z in range(0,2):
        for y in range(0,3):
            for x in range(0,4):
                soma = lvn.soma_vetores(vetor_pos,vetor_dir)
                sub = lvn.subtrai_vetores(soma,[x,y,z])
                print(lvn.produto_escalar3(soma,sub))
                if lvn.produto_escalar3(soma,sub) > 0:
                    achou = False
                    vetor_atul = [x,y,z]
                    while not achou:
                        # print(matriz_mun[z][y][x])
                        if matriz_mun[z][y][x] == 1:
                            if vetor_atul[0] < 6 and vetor_atul[1] < 5:
                                matriz_vis[vetor_atul[1]][vetor_atul[0]] = '#'
                                achou = True
                        else:
                            vetor_atul = lvn.soma_vetores(vetor_atul,[1,1,1])
                        if vetor_atul[0] < 6 or vetor_atul[1] < 5 or vetor_atul[2] < 3:
                            achou = True
def Desenha_matriz_visual():
    global matriz_vis
    for c in matriz_vis:
        for v in c:
            print('\033[0;0;43m',v,'\033[m',end='')
        print()
def main():
    RayTracing()
    Desenha_matriz_visual()
main()