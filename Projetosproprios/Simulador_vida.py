import LibraryVectorNatan as lvn
import math


mundo = [[0,0,0,2,0,0,0],
         [0,0,0,0,0,0,0],
         [0,2,0,0,0,2,0],
         [0,0,0,0,0,0,0],
         [0,0,0,2,0,0,0],]


neuronios_registro = [1,2,3,4,5,6]
conexoes_registro = []
fome = 1


vetor_pos = [3,2]
vetor_dir = [1,0]


#------------------------------------------------------------
#                       CÉREBRO DO SER
#Procura oque precisa:hipotálamo;função:processamento_fome()
#------------------------------------------------------------

#visão,tato,audição,olfato


def processamento_fome():
    global fome,vetor_pos,vetor_dir
    c = None
    for c in conexoes_registro:
        pass
    if c[2]["fome"] == 1:
        for conexao in conexoes_registro:
            if conexao[2]["tato"] == 1:
                fome = 0
                if vetor_pos[1] + 1 < 5 and vetor_pos[0] < 7:
                    if mundo[vetor_pos[1] + 1][vetor_pos[0]] == 2:
                        mundo[vetor_pos[1] + 1][vetor_pos[0]] = 0

                if vetor_pos[1] < 5 and vetor_pos[0] + 1 < 7:
                    if mundo[vetor_pos[1]][vetor_pos[0] + 1] == 2:
                        mundo[vetor_pos[1]][vetor_pos[0] + 1] = 0
                        print("aconteceu")

                if vetor_pos[1] - 1 >= 0 and vetor_pos[0] < 7:
                    if mundo[vetor_pos[1] - 1][vetor_pos[0]] == 2:
                        mundo[vetor_pos[1] - 1][vetor_pos[0]] = 0

                if vetor_pos[1] < 5 and vetor_pos[0] - 1 >= 0:
                    if mundo[vetor_pos[1]][vetor_pos[0] - 1] == 2:
                        mundo[vetor_pos[1]][vetor_pos[0] - 1] = 0

                cria_conexao_registro(
                    {"visão": None, "tato": None, "audição": None,
                     "olfato": None, "direção": vetor_dir,
                     "fome": fome,"pos":vetor_pos})


            if conexao[2]["visão"] == 1 and conexao[2]["tato"] == 0:
                mundo[vetor_pos[1]][vetor_pos[0]] = 0
                vetor_pos = lvn.soma_vetores(vetor_pos,conexao[2]["direção"])
                cria_conexao_registro(
                    {"visão": None, "tato": None, "audição": None,
                     "olfato": None, "direção": vetor_dir,
                     "fome": fome,"pos":vetor_pos})
                mundo[vetor_pos[1]][vetor_pos[0]] = 1


            if conexao[2]["visão"] == 0 and conexao[2]["tato"] == 0:
                if vetor_dir == [1,0]:
                    vetor_dir = [0,1]
                    cria_conexao_registro(
                        {"visão": None, "tato": None, "audição": None,
                         "olfato": None, "direção": vetor_dir,
                         "fome": fome,"pos":vetor_pos})
                    return
                if vetor_dir == [0,1]:
                    vetor_dir = [-1,0]
                    cria_conexao_registro(
                        {"visão": None, "tato": None, "audição": None,
                         "olfato": None, "direção": vetor_dir,
                         "fome": fome,"pos":vetor_pos})
                    return
                if vetor_dir == [-1,0]:
                    vetor_dir = [0,-1]
                    cria_conexao_registro(
                        {"visão": None, "tato": None, "audição": None,
                         "olfato": None, "direção": vetor_dir,
                         "fome": fome,"pos":vetor_pos})
                    return
                if vetor_dir == [0,-1]:
                    vetor_dir = [1,0]
                    cria_conexao_registro(
                        {"visão": None, "tato": None, "audição": None,
                         "olfato": None, "direção": vetor_dir,
                         "fome": fome,"pos":vetor_pos})
                    return


def cria_conexao_registro(estimulos):
    global conexoes_registro,neuronios_registro
    neuronio_2 = []
    for pos0,c in enumerate(neuronios_registro):
        if len(neuronio_2) == 2:
            neuronio_2.append(estimulos)
            conexoes_registro.append(neuronio_2)
            break
        if len(neuronio_2) != 2:
            neuronio_2.append(c)


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


def sentido_olfato():
    global mundo, vetor_pos
    resposta = 0
    for y,c in enumerate(mundo):
        for x,v in enumerate(c):
            if v == 2:
                resposta = 1+(3-round(math.sqrt((vetor_pos[0]-x)**2+(vetor_pos[1]-y)**2)))
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


def mostra_conexoes():
    global conexoes_registro
    for c in conexoes_registro:
        print(f"{c[0]};{c[1]};{c[2]}")


def main():
    global conexoes_registro,vetor_dir
    for i in range(0,3):
        mundo[vetor_pos[1]][vetor_pos[0]] = 1
        respostas_sentido = []
        respostas_nomeacoes = ["visão","tato","audição","olfato"]
        respostas_sentido.append(sentido_visao())
        respostas_sentido.append(sentido_tato())
        respostas_sentido.append(sentido_audicao())
        respostas_sentido.append(sentido_olfato())


        for pos0,c in enumerate(respostas_sentido):
            print(f"{respostas_nomeacoes[pos0]}:{c}",end=';')
        print()


        cria_conexao_registro({"visão":respostas_sentido[0],"tato":respostas_sentido[1],"audição":respostas_sentido[2],"olfato":respostas_sentido[3],"direção":vetor_dir,
                               "fome":fome,"pos":vetor_pos})


        processamento_fome()


        mostra_conexoes()


        desenha_mundo()

        print(fome)

main()