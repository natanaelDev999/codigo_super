import LibraryVectorNatan as lvn
import math


mundo = [[0,0,0,2,0,0,0],
         [0,0,0,0,0,0,0],
         [0,2,0,0,0,2,0],
         [0,0,0,0,0,0,0],
         [0,0,0,2,0,0,0],]


vetor_pos = [2,2]
vetor_dir = [1,0]


def sentido_visao():
    global mundo, vetor_pos, vetor_dir
    vetor_atu = vetor_pos[:]
    resposta = 0
    while True:
        if vetor_atu[1] < 5 and  vetor_atu[0] < 7:
            print(vetor_atu[1],vetor_atu[0])
            if mundo[vetor_atu[1]][vetor_atu[0]] == 2:
                resposta = 1
                break
            else:
                vetor_atu = lvn.soma_vetores(vetor_atu,vetor_dir)
                vetor_atu = [round(vetor_atu[0]),round(vetor_atu[1])]
        else:
            break
    return resposta


def sentido_audicao():
    global mundo, vetor_pos
    resposta = 0
    for y,c in enumerate(mundo):
        for x,v in enumerate(c):
            if v == 4:
                if round(math.sqrt((vetor_pos[0]-x)**2+(vetor_pos[1]-y)**2)) <= 1.5:
                    resposta = 1
    return resposta


def sentido_tato():
    global mundo, vetor_pos
    resposta = 0
    if vetor_pos[1]+1 < 5 and vetor_pos[0] < 7:
        if mundo[vetor_pos[1]+1][vetor_pos[0]] == 2:
            resposta = 1

    if vetor_pos[1] < 5 and vetor_pos[0]+1 < 7:
        if mundo[vetor_pos[1]][vetor_pos[0]+1] == 2:
            resposta = 1

    if vetor_pos[1]-1 >= 0 and vetor_pos[0] < 7:
        if mundo[vetor_pos[1]-1][vetor_pos[0]] == 2:
            resposta = 1

    if vetor_pos[1] < 5 and vetor_pos[0]-1 >= 0:
        if mundo[vetor_pos[1]][vetor_pos[0]-1] == 2:
            resposta = 1
    return resposta


def desenha_mundo():
    global mundo
    for c in mundo:
        for v in c:
            print(v,end=' ')
        print()


def main():
    mundo[vetor_pos[1]][vetor_pos[0]] = 1
    respostas_sentido = []
    respostas_sentido.append(sentido_visao())
    respostas_sentido.append(sentido_tato())
    respostas_sentido.append(sentido_audicao())
    print(respostas_sentido)
    desenha_mundo()

main()