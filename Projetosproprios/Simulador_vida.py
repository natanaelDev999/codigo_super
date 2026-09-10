import LibraryVectorNatan as lvn
import math


mundo = [[0,0,0,2,0,0,0],
         [0,0,0,0,0,0,0],
         [0,2,0,0,0,2,0],
         [0,0,0,0,0,0,0],
         [0,0,0,2,0,0,0],]


neuronios_carga_resultado = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
neuronios_resultado =       [1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20]
conexoes_resultado = []


neuronios_carga_registro =  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
neuronios_registro =        [1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20]
conexoes_registro =  []
fome = 1
sinapses_limites = 8


vetor_pos = [3,2]
vetor_dir = [1,0]


#------------------------------------------------------------
#                       CÉREBRO DO SER
#Procura oque precisa:processamento_fome()
#Trata com oque sabe:processamento_resultados
#------------------------------------------------------------

#visão,tato,audição,olfato


def processamento_resultados():
    global conexoes_resultado,conexoes_registro,vetor_dir
    estado_momento = None
    for c in conexoes_registro:
        estado_momento = c[:]
    for conexao in conexoes_resultado:
        if estado_momento[2]["visão"] != conexao[2]["visão"]:
            if vetor_dir == [1, 0]:
                vetor_dir = [0, 1]
                cria_conexao_registro(
                    {"visão": None, "tato": None, "audição": None,
                     "olfato": None, "direção": vetor_dir,
                     "fome": fome, "pos": vetor_pos})
            elif vetor_dir == [0, 1]:
                vetor_dir = [-1, 0]
                cria_conexao_registro(
                    {"visão": None, "tato": None, "audição": None,
                     "olfato": None, "direção": vetor_dir,
                     "fome": fome, "pos": vetor_pos})
            elif vetor_dir == [-1, 0]:
                vetor_dir = [0, -1]
                cria_conexao_registro(
                    {"visão": None, "tato": None, "audição": None,
                     "olfato": None, "direção": vetor_dir,
                     "fome": fome, "pos": vetor_pos})

            elif vetor_dir == [0, -1]:
                vetor_dir = [1, 0]
                cria_conexao_registro(
                    {"visão": None, "tato": None, "audição": None,
                     "olfato": None, "direção": vetor_dir,
                     "fome": fome, "pos": vetor_pos})



def processamento_fome():
    global fome,vetor_pos,vetor_dir
    c = None
    for c in conexoes_registro:
        pass
    if c[2]["fome"] == 1:
        for conexao in conexoes_registro:
            if conexao == conexoes_registro[-1]:
                if conexao[2]["tato"] == 1:
                    fome = 0
                    if vetor_pos[1] + 1 < 5 and vetor_pos[0] < 7:
                        if mundo[vetor_pos[1] + 1][vetor_pos[0]] == 2:
                            mundo[vetor_pos[1] + 1][vetor_pos[0]] = 0

                    if vetor_pos[1] < 5 and vetor_pos[0] + 1 < 7:
                        if mundo[vetor_pos[1]][vetor_pos[0] + 1] == 2:
                            mundo[vetor_pos[1]][vetor_pos[0] + 1] = 0

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
    global conexoes_registro,neuronios_registro,neuronios_carga_registro
    neuronio_2 = []
    anterior = None
    if len(conexoes_registro) > 0:
        anterior = conexoes_registro[-1]
    for pos0, c in enumerate(neuronios_registro):
        if len(neuronio_2) == 2:
            neuronio_2.append(estimulos)
            if anterior != None:
                if anterior[2] != neuronio_2[2]:
                    conexoes_registro.append(neuronio_2)
            else:
                conexoes_registro.append(neuronio_2)
            break
        if len(neuronio_2) != 2:
            if neuronios_carga_registro[pos0] < sinapses_limites:
                neuronios_carga_registro[pos0] += 1
                neuronio_2.append(c)


def cria_conexao_resultado():
    global conexoes_registro, neuronios_resultado, neuronios_carga_registro,conexoes_resultado,sinapses_limites
    neuronio_2 = []
    anterior = None
    if len(conexoes_resultado) > 0:
        anterior = conexoes_resultado[-1]
    for pos0,neuronio in enumerate(neuronios_resultado):
        if len(neuronio_2) != 2:
            if neuronios_carga_resultado[pos0] < sinapses_limites:
                neuronios_carga_resultado[pos0] += 1
                neuronio_2.append(neuronio)
        if len(neuronio_2) == 2:
            neuronio_2.append({})
            for conexao in conexoes_registro:
                if conexao[2]["visão"] == 1:
                    # estrutura: [estimulos(que trouxeram algo bom)]
                    neuronio_2[2] = conexao[2]
            if anterior != None:
                if anterior[2] != neuronio_2[2]:
                    if len(neuronio_2[2]) != 0:
                        conexoes_resultado.append(neuronio_2)
            else:
                if len(neuronio_2[2]) != 0:
                    conexoes_resultado.append(neuronio_2)
            anterior = neuronio_2
            neuronio_2 = []


def sentido_visao():
    global mundo, vetor_pos, vetor_dir
    vetor_atu = vetor_pos[:]
    resposta = 0
    while True:
        if vetor_atu[1] < 5 and  vetor_atu[0] < 7 and vetor_atu[1] > 0 and vetor_atu[0] > 0:
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


def mostra_conexoes_registro():
    global conexoes_registro
    for c in conexoes_registro:
        print(f"{c[0]};{c[1]};{c[2]}")


def mostra_conexoes_resultado():
    global conexoes_resultado
    for c in conexoes_resultado:
        print(f"\033[31m{c[0]};{c[1]};{c[2]}\033[m")


def main():
    global conexoes_registro,vetor_dir,fome
    for i in range(0,10):
        mundo[vetor_pos[1]][vetor_pos[0]] = 1
        if i == 0:
            desenha_mundo()
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


        processamento_resultados()


        processamento_fome()


        cria_conexao_resultado()


        mostra_conexoes_registro()


        mostra_conexoes_resultado()


        desenha_mundo()

        print(fome)

        if i == 2:
            fome = 1

main()