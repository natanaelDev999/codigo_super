import os
import time

visao = [[' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ','=',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],]

pontos = [[3,0]]
velocidades = [0]

def atua_gravidade():
    global pontos,velocidades, visao
    for pos0,p in enumerate(pontos):
        if p[0] < 6 and p[1] < 6:
            if p[1]+1 < 8:
                if visao[p[1]+1][p[0]] == ' ':
                    visao[p[1]][p[0]] = ' '

                    p[1] += 1

                    visao[p[1]][p[0]] = '\033[31m0\033[m'

                    velocidades[pos0] += 1
                else:
                    if velocidades[pos0] > 0:
                        if p[1] - 1 > 0:
                            visao[p[1]][p[0]] = ' '

                            p[1] -= 1

                            visao[p[1]][p[0]] = '\033[31m0\033[m'

                            velocidades[pos0] -= 2
        else:
            if velocidades[pos0] > 0:
                if p[1]-1 > 0:
                    visao[p[1]][p[0]] = ' '

                    p[1] -= 1

                    visao[p[1]][p[0]] = '\033[31m0\033[m'

                    velocidades[pos0] -= 1
        print(velocidades[pos0],' ',p)

def renderiza_particulas():
    global pontos
    for c in pontos:
        visao[c[1]][c[0]] = '\033[31m0\033[m'
def desenha_visao():
    global visao
    for c in visao:
        for v in c:
            print(v,end=' ')
        print()
def main():

    renderiza_particulas()

    while True:
        desenha_visao()
        atua_gravidade()
        time.sleep(1)
        os.system('cls')

main()