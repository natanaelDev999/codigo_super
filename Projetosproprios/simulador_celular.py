import LibraryVectorNatan as lvn
import math

mundo = [[' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' ']]

particulas_a = [[5,5],[3,5],[5,3],[3,1],[5,1],[1,1],[1,3],[1,5]]
particulas_b = [[3,3]]

def desenha_particulas_a():
    global particulas_a
    for v in particulas_a:
        mundo[v[1]][v[0]] = '1'

def desenha_particulas_b():
    global particulas_b
    for v in particulas_b:
        mundo[v[1]][v[0]] = '2'

def trata_particulas_a():
    global mundo
    for pos0,c in enumerate(mundo):
        for pos1,v in enumerate(c):
            if v == '1':
                print([pos1, pos0])
                vetor_pos1 = []
                vetor_pos2 = []
                vetor_dir = [0, 0]
                vetor_pos1 = [pos1,pos0]
                for pos2,c2 in enumerate(mundo):
                    for pos3,v2 in enumerate(c2):
                        if v2 == '2':
                            vetor_pos2 = [pos3,pos2]
                            break
                if len(vetor_pos1) > 0 and len(vetor_pos2) > 0:
                    deltaX = vetor_pos1[0] - vetor_pos2[0]
                    deltaY = vetor_pos1[1] - vetor_pos2[1]
                    dist = math.sqrt(deltaX**2+deltaY**2)
                    if dist <= 3:
                        if deltaX < 0:
                            vetor_dir[0] = 1
                        if deltaX > 0:
                            vetor_dir[0] = -1
                        if deltaY < 0:
                            vetor_dir[1] = 1
                        if deltaY > 0:
                            vetor_dir[1] = -1
                        vetor_novo = lvn.soma_vetores(vetor_dir,vetor_pos1)
                        if vetor_novo[0] < 8 and vetor_novo[1] < 10:
                            if mundo[vetor_novo[1]][vetor_novo[0]] == ' ':
                                mundo[vetor_novo[1]][vetor_novo[0]] = '1'
                                mundo[vetor_pos1[1]][vetor_pos1[0]] = ' '


def desenha_mundo():
    global mundo
    for c in mundo:
        for v in c:
            print(v,end=' ')
        print()

def main():
    global mundo
    desenha_particulas_a()
    desenha_particulas_b()
    desenha_mundo()
    trata_particulas_a()
    print('-----------------------------------')
    desenha_mundo()

main()