import LibraryVectorNatan as lvn
#vetores
vetor_pos = [0,0,0]
vetor_dir = [-2,0,1]
#raytracing variáveis
y_visao = 4
x_visao = 4
#mundo
matriz_mun = [
    [
        [0,0,0,0],
        [0,1,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ],
    [
        [0,0,0,0],
        [0,1,0,0],
        [0,0,1,0],
        [0,0,0,0]
    ],
    [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ],
    [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
]
#visão
matriz_visual = [[' ',' ',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ',' ',' ']]
def raytracing():
    global vetor_pos,vetor_dir,x_visao,y_visao
    for y in range(0,y_visao):
        for x in range(0,x_visao):
            vetor_ini = [x+vetor_pos[0],y+vetor_pos[1],vetor_pos[2]]
            while True:
                if vetor_ini[2] < 4 and vetor_ini[1] < 4 and vetor_ini[0] < 4 and vetor_ini[2] > 0 and vetor_ini[1] > 0 and vetor_ini[0] > 0:
                    if matriz_mun[vetor_ini[2]][vetor_ini[1]][vetor_ini[0]] == 1:
                        matriz_visual[vetor_ini[1]][vetor_ini[0]] = '#'
                        break
                    else:
                        vetor_ini = lvn.soma_vetores(vetor_ini,vetor_dir)
                        print(vetor_ini)
                else:
                    vetor_ini = lvn.soma_vetores(vetor_ini, vetor_dir)
                    print(vetor_ini)
                if vetor_ini[2] == 4 or vetor_ini[2] < 0:
                    break

def desenha_tela():
    global matriz_visual
    for c in matriz_visual:
        for v in c:
            print('\033[0;0;43m',v,'\033[m',end='')
        print()

def main():
    raytracing()
    desenha_tela()
main()