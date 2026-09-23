import math
import LibraryVectorNatan

tela = [[' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ']]

x_pixel = 9
y_pixel = 11

distancia = 10

vetor_pos = [0,0,0]
vetor_dir = [0,0,1]

esferas = [{"x":0,"y":0,"z":3,"r":2}]

def raytracing():
    global x_pixel,y_pixel,esferas,vetor_pos,vetor_dir,tela,distancia
    for i in range(0,y_pixel-1):
        for j in range(0,x_pixel-1):
            ponto_atual = LibraryVectorNatan.soma_vetores(
                LibraryVectorNatan.soma_vetores(vetor_pos,vetor_dir),
                [j,i,0]
                )
            while True:
                for v in esferas:
                    if math.sqrt((ponto_atual[0]-v["x"])**2+(ponto_atual[1]-v["y"])**2+(ponto_atual[2]-v["z"])**2) <= v["r"]:
                        if int(ponto_atual[1]+(y_pixel/2)) < y_pixel and int(ponto_atual[0]+(x_pixel/2)) < x_pixel:
                            tela[int(ponto_atual[1]+(y_pixel/2))][int(ponto_atual[0]+(x_pixel/2))] = '\033[31m#\033[m'
                        break
                if ponto_atual[1] < y_pixel and ponto_atual[0] < x_pixel and ponto_atual[2] < distancia:
                    ponto_atual = LibraryVectorNatan.soma_vetores(ponto_atual,vetor_dir)
                else:
                    break

def desenha_tela():
    global tela
    for c in tela:
        for v in c:
            print(v,end=' ')
        print()

def main():
    raytracing()
    desenha_tela()
main()