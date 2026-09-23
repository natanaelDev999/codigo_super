import math
import LibraryVectorNatan as lvt

tela = []

vetor_pos = [0,0,0]
vetor_dir = [0,0,1]

esfera = [[0,0,3,6]]

y_tela = 10
x_tela = 10

def raytracing():
    global tela,y_tela,x_tela,vetor_pos,vetor_dir,esfera
    for c in range(0,y_tela*2):
        for v in range(0,x_tela*2):
            ponto = lvt.soma_vetores(lvt.soma_vetores(vetor_pos,vetor_dir),[c,v,0])
            cont = 0
            while True:
                for i in esfera:
                    if math.sqrt((i[0]-ponto[0])**2+
                                 (i[1]-ponto[1])**2+
                                 (i[2]-ponto[2])**2) < i[3]:
                        tela[int((ponto[1]+(y_tela/2)))][int((ponto[0]+(x_tela/2)))] = '\033[38;2;255;0;0m█\033[m'
                        break
                cont += 1
                if cont < 4:
                    ponto = lvt.soma_vetores(ponto,vetor_dir)
                else:
                    break

def cria_tela():
    global tela,y_tela,x_tela
    for c in range(0,y_tela):
        tela.append([])
        for v in range(0,x_tela):
            tela[c].append(' ')
def desenha_tela():
    global tela
    for c in tela:
        for v in c:
            print(v,end=' ')
        print()
def main():
    cria_tela()
    raytracing()
    desenha_tela()
main()