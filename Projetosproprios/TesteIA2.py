import random
# camadas
camadas = [{'distancias':[],'biases':[],'no':[],'n_no':0,'n_et':0},
           {'distancias':[],'biases':[],'no':[],'n_no':0,'n_et':0},
           {'distancias':[],'biases':[],'no':[],'n_no':0,'n_et':0}]

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
    for c in range(camadas[pos]['n_no']):
        if camadas[pos]['no'][c] < 0:
            camadas[pos]['no'][c] = 0
        else:
            if camadas[pos]['no'][c] > 0.5:
                camadas[pos]['no'][c] = 1
            else:
                camadas[pos]['no'][c] = 0
#
def inicia_camadas():
    # camada 1
    ini_camadas(0,2,4)
    # camada 2
    ini_camadas(1,4,4)
    # camada para saída
    ini_camadas(2,4,2)
    #
# função cerebral
def cerebro(entradas,pos1,pos2,pos3):
    global camadas
    # camada 1
    avanca(pos1,entradas)
    ativacao(pos1)
    # camada 2
    avanca(pos2, camadas[pos1]['no'])
    ativacao(pos2)
    # camada para saída
    avanca(pos3, camadas[pos2]['no'])
    ativacao(pos3)

    return camadas[pos3]['no']

# função principal
def main():

    entradas = [0,1]

    inicia_camadas()
    resul = cerebro(entradas,0,1,2)
    print(camadas[0])
    print(camadas[1])
    print(camadas[2])
    print(resul)

main()