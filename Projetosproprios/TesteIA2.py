import random
import json
import LibraryVectorNatan as lvn
import os
import time
# valores de aprendizado
valores_aprendizado= [0,0,0,0]
# camadas
camadas = [{'distancias':[],'biases':[],'no':[],'n_no':0,'n_et':0},
           {'distancias':[],'biases':[],'no':[],'n_no':0,'n_et':0},
           {'distancias':[],'biases':[],'no':[],'n_no':0,'n_et':0}]
# limpa camadas
def limpa_camadas():
    global camadas
    for c in camadas:
        c['biases'] = []
        c['distancias'] = []
# inicia camada
def ini_camadas(pos,entradas,nos):
    global camadas
    for c in range(nos):
        camadas[pos]['distancias'].append([])
        for d in range(entradas):
            camadas[pos]['distancias'][c].append(random.uniform(1,-1))
    for i in range(nos):
        camadas[pos]['biases'].append(random.uniform(1,-1))
        camadas[pos]['no'].append(0.)
    camadas[pos]['n_no'] = nos
    camadas[pos]['n_et'] = entradas
# função para avançar
def avanca(pos,entradas):
    global camadas

    camadas[pos]['no'] = []


    for j in range(camadas[pos]['n_no']):
        camadas[pos]['no'].append(0.)

    for c in range(camadas[pos]['n_no']):
        # soma das distâncias com as entradas
        for v in range(camadas[pos]['n_et']):
            #print(camadas[pos]['distancias'][c])
            camadas[pos]['no'][c] += camadas[pos]['distancias'][c][v] * entradas[v]

        # adiciona o bias
        camadas[pos]['no'][c] += camadas[pos]['biases'][c]
# função de ativação
def ativacao(pos):
    novo_no = []
    for c in range(camadas[pos]['n_no']):
        if camadas[pos]['no'][c] < 0:
            novo_no.append(0)
        else:
            if camadas[pos]['no'][c] > 0.5:
                novo_no.append(1)

            else:
                novo_no.append(0)
    return novo_no
#
def inicia_camadas():
    # camada 1
    ini_camadas(0,2,4)
    # camada 2
    ini_camadas(1,4,4)
    # camada para saída
    ini_camadas(2,4,2)
    #
# função para aprendizado
def aprendizado(camada_modificada):
    global valores_aprendizado
    '''saida = camadas[-1]['no']
    erro = lvn.subtrai_vetores(saida_esperada,saida)
    print(camadas[camada_modificada]['biases'])
    for pos0,c in enumerate(camadas[camada_modificada]['biases']):
         camadas[camada_modificada]['biases'][pos0] += erro[0]+erro[1]
    print(camadas[camada_modificada]['biases'])'''
    random.seed(None)
    for pos0, c in enumerate(camadas[camada_modificada]['biases']):
        valor = random.random()*2
        camadas[camada_modificada]['biases'][pos0] /= valor
        valores_aprendizado[pos0] += valor
    random.seed(250000)
# função cerebral
def cerebro(entradas,pos1,pos2,pos3):
    global camadas
    # camada 1
    avanca(pos1,entradas)
    no1 = ativacao(pos1)
    # camada 2
    avanca(pos2, no1)
    no2 = ativacao(pos2)
    # camada para saída
    avanca(pos3, no2)
    no3 = ativacao(pos3)

    return no3
# função para salvamento de informações para escolha dos valores corretos
def armazena_dados_seed(seed):
    global camadas,valores_aprendizado
    dados_json = {}
    with open('camadas_testeIA2.json','r') as arquivo1:
        dados_json = json.load(arquivo1)
    dados_json['camada2']=valores_aprendizado
    with open('camadas_testeIA2.json','w') as arquivo2:
        json.dump(dados_json,arquivo2)
#================================================================
#                     PARTE QUE TRATA DO SER
mundo = [[' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ','c',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' '],]
# informações do ser
vetor_pos = [2,2]
vetor_dir = [1,0]
fome = 1
# vetor para ações
vetor_acoes = ['^','a']
# funções para os sentidos que serão as entradas

def sentido_visao():
    global mundo, vetor_pos, vetor_dir
    vetor_atu = vetor_pos[:]
    resposta = 0
    while True:
        if vetor_atu[1] < 5 and  vetor_atu[0] < 7 and vetor_atu[1] > 0 and vetor_atu[0] > 0:
            if mundo[vetor_atu[1]][vetor_atu[0]] == 'c':
                resposta = 1
                break
            else:
                vetor_atu = lvn.soma_vetores(vetor_atu,vetor_dir)
                vetor_atu = [round(vetor_atu[0]),round(vetor_atu[1])]
        else:
            break
    return resposta

def sentido_tato():
    global mundo, vetor_pos
    resposta = 0
    if vetor_pos[1]+1 < 5 and vetor_pos[0]+1 < 7:
        if mundo[vetor_pos[1]+1][vetor_pos[0]+1] == 'c':
            resposta = 1

    if vetor_pos[1]-1 >= 0 and vetor_pos[0]-1 < 7:
        if mundo[vetor_pos[1]-1][vetor_pos[0]-1] == 'c':
            resposta = 1

    if vetor_pos[1]+1 < 5 and vetor_pos[0]-1 < 7:
        if mundo[vetor_pos[1]+1][vetor_pos[0]-1] == 'c':
            resposta = 1

    if vetor_pos[1]-1 < 5 and vetor_pos[0]+1 < 7:
        if mundo[vetor_pos[1]-1][vetor_pos[0]+1] == 'c':
            resposta = 1




    if vetor_pos[1]+1 < 5 and vetor_pos[0] < 7:
        if mundo[vetor_pos[1]+1][vetor_pos[0]] == 'c':
            resposta = 1

    if vetor_pos[1] < 5 and vetor_pos[0]+1 < 7:
        if mundo[vetor_pos[1]][vetor_pos[0]+1] == 'c':
            resposta = 1

    if vetor_pos[1]-1 >= 0 and vetor_pos[0] < 7:
        if mundo[vetor_pos[1]-1][vetor_pos[0]] == 'c':
            resposta = 1

    if vetor_pos[1] < 5 and vetor_pos[0]-1 >= 0:
        if mundo[vetor_pos[1]][vetor_pos[0]-1] == 'c':
            resposta = 1
    return resposta

def desenha_mundo():
    global mundo
    for c in mundo:
        for v in c:
            print(v,end=' ')
        print()

def movimento_frontal():
    global vetor_pos,vetor_dir
    novo_vetor = lvn.soma_vetores(vetor_pos,vetor_dir)
    if novo_vetor[0] < 7 and novo_vetor[1] < 5 and mundo[novo_vetor[1]][novo_vetor[0]] != 'c':
        vetor_pos = novo_vetor[:]

def come_alimento():
    global vetor_pos
    if vetor_pos[1]+1 < 5 and vetor_pos[0]+1 < 7:
        if mundo[vetor_pos[1]+1][vetor_pos[0]+1] == 'c':
            mundo[vetor_pos[1] + 1][vetor_pos[0] + 1] = ' '
            return

    if vetor_pos[1]-1 >= 0 and vetor_pos[0]-1 < 7:
        if mundo[vetor_pos[1]-1][vetor_pos[0]-1] == 'c':
            mundo[vetor_pos[1]-1][vetor_pos[0]-1] = ' '
            return

    if vetor_pos[1]+1 < 5 and vetor_pos[0]-1 < 7:
        if mundo[vetor_pos[1]+1][vetor_pos[0]-1] == 'c':
            mundo[vetor_pos[1]+1][vetor_pos[0]-1] = ' '
            return

    if vetor_pos[1]-1 < 5 and vetor_pos[0]+1 < 7:
        if mundo[vetor_pos[1]-1][vetor_pos[0]+1] == 'c':
            mundo[vetor_pos[1]-1][vetor_pos[0]+1] = ' '
            return




    if vetor_pos[1]+1 < 5 and vetor_pos[0] < 7:
        if mundo[vetor_pos[1]+1][vetor_pos[0]] == 'c':
            mundo[vetor_pos[1]+1][vetor_pos[0]] = ' '
            return

    if vetor_pos[1] < 5 and vetor_pos[0]+1 < 7:
        if mundo[vetor_pos[1]][vetor_pos[0]+1] == 'c':
            mundo[vetor_pos[1]][vetor_pos[0]+1] = ' '
            return

    if vetor_pos[1]-1 >= 0 and vetor_pos[0] < 7:
        if mundo[vetor_pos[1]-1][vetor_pos[0]] == 'c':
            mundo[vetor_pos[1]-1][vetor_pos[0]] = ' '
            return

    if vetor_pos[1] < 5 and vetor_pos[0]-1 >= 0:
        if mundo[vetor_pos[1]][vetor_pos[0]-1] == 'c':
            mundo[vetor_pos[1]][vetor_pos[0]-1] = ' '
            return

#================================================================

# função principal
def main():
    global vetor_pos,vetor_acoes,fome

    SEED = 250000

    mundo[vetor_pos[1]][vetor_pos[0]] = 'S'

    for c in range(9):
        print(c)
        desenha_mundo()
        mundo[vetor_pos[1]][vetor_pos[0]] = ' '
        entradas = [sentido_visao(),sentido_tato()]

        random.seed(SEED)

        limpa_camadas()
        inicia_camadas()
        aprendizado(1)
        resul = cerebro(entradas,0,1,2)

        print(resul)
        for pos0,v in enumerate(resul):
            if v == 1:
                if vetor_acoes[pos0] == 'a' and fome == 1:
                    come_alimento()
                    fome = 0
                if vetor_acoes[pos0] == '^':
                    movimento_frontal()
        mundo[vetor_pos[1]][vetor_pos[0]] = 'S'
        time.sleep(1)
        os.system('cls')

    salva = str(input('Deve ser salvo: ')).upper()

    if salva == 'S':
        armazena_dados_seed(SEED)


    # # Vamos testar 250.000 combinações de seeds diferentes
    # for SEED_TESTE in range(250000,300000):
    #     random.seed(SEED_TESTE)
    #     inicia_camadas()
    #
    #     # Condição 1: Vê comida (perto, ex: dist=1), mas não toca.
    #     # Esperado: Andar [1, 0] ou [1, 1]
    #     resul_visao = cerebro([1, 0], 0, 1, 2)
    #
    #     # Condição 2: Não vê comida, mas sente pelo tato.
    #     # Esperado: Comer [0, 1] ou [1, 1]
    #     resul_tato = cerebro([0, 1], 0, 1, 2)
    #
    #     # Verifica se o cérebro tomou as decisões certas:
    #     # resul_visao[0] == 1 (anda) e resul_tato[1] == 1 (come)
    #     if resul_visao[0] == 1 and resul_tato[1] == 1:
    #         print(f"SEED PERFEITO ENCONTRADO: {SEED_TESTE}")
    #         print(f"Ao ver comida: {resul_visao} (Anda)")
    #         print(f"Ao tocar na comida: {resul_tato} (Come)")
    #         break
    #     print(SEED_TESTE)
    #     camadas = [{'distancias': [], 'biases': [], 'no': [], 'n_no': 0, 'n_et': 0},
    #                {'distancias': [], 'biases': [], 'no': [], 'n_no': 0, 'n_et': 0},
    #                {'distancias': [], 'biases': [], 'no': [], 'n_no': 0, 'n_et': 0}]

main()