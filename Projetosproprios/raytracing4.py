import math
import LibraryVectorNatan as lvn
tela = []
raios = []
# tamanho , pos
esferas = [[8,[0,0,8]]]
def colisao_esfera(raio):
    global esferas
    for c in esferas:
        print(c[1])
        if math.sqrt((c[1][0]-raio[0])**2+(c[1][1]-raio[1])**2+(c[1][2]-raio[2])**2) < c[0]:
            return ' '
    return '#'
def tracado_raios(dist,dir):
    global raios,tela
    for y,l in enumerate(raios):
        for x, c in enumerate(l):
            atual_raio = c[:]
            for v in range(dist):
                atual_raio = lvn.soma_vetores(atual_raio,dir)
                tela[y][x] = colisao_esfera(atual_raio)

def gera_raios(x_r,y_r):
    global raios
    for y in range(0,y_r):
        raios.append([])
        for x in range(0,x_r):
            x_pixel = x
            y_pixel = y
            if x <= x_r/2:
                x_pixel = -x_pixel
            if y <= y_r/2:
                y_pixel = -y_pixel

            if x >= x_r/2:
                x_pixel = x_r-x_pixel
            if y >= y_r/2:
                y_pixel = y_r-y_pixel
            raios[y].append([x_pixel,y_pixel,0])
def cria_tela(x,y):
    global tela
    for c in range(y):
        tela.append([])
        for v in range(x):
            tela[c].append(' ')
def desenha_tela():
    global tela
    for c in tela:
        for v in c:
            print(v,end=' ')
        print()
def main():
    cria_tela(20,20)
    gera_raios(20,20)
    tracado_raios(5,[0,0,1])
    desenha_tela()
main()