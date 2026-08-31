#---------------------------------------------------------------------
#                         LIBRARYVECTORNATAN
#---------------------------------------------------------------------
#                            BIBLIOTECAS
import math
#---------------------------------------------------------------------
#biblioteca para manipulação de vetores
#---------------------------------------------------------------------
#                        OPERAÇÕES MATEMÁTICAS
#---------------------------------------------------------------------
# soma de vetores
def soma_vetores(vetor1,vetor2):
    '''

    :param vetor1: pode ser uma tupla ou lista será usada para soma
    :param vetor2: pode ser uma tupla ou lista será usada para soma
    :return: retorna a soma dos dois vetores
    '''
    vetor_saida = []
    for pos0,i in enumerate(vetor1):
        vetor_saida.append(vetor2[pos0]+i)
    return vetor_saida
# subtração de vetores
def subtrai_vetores(vetor1,vetor2):
    '''

    :param vetor1: pode ser uma tupla ou lista será usada para subtração
    :param vetor2: pode ser uma tupla ou lista será usada para subtração
    :return: retorna a subtração dos dois vetores
    '''
    vetor_saida = []
    for pos0,i in enumerate(vetor1):
        vetor_saida.append(i-vetor2[pos0])
    return vetor_saida
# multiplicação de vetores
def multiplica_vetores(vetor1,vetor2):
    '''

    :param vetor1: pode ser uma tupla ou lista será usada para multiplicação
    :param vetor2: pode ser uma tupla ou lista será usada para multiplicação
    :return: retorna a multiplicação dos dois vetores
    '''
    vetor_saida = []
    for pos0, i in enumerate(vetor1):
        vetor_saida.append(i * vetor2[pos0])
    return vetor_saida
# divisão de vetores
def divide_vetores(vetor1,vetor2):
    '''

    :param vetor1: pode ser uma tupla ou lista será usada para divisão
    :param vetor2: pode ser uma tupla ou lista será usada para divisão
    :return: retorna a divisão dos dois vetores
    '''
    vetor_saida = []
    for pos0, i in enumerate(vetor1):
        vetor_saida.append(i / vetor2[pos0])
    return vetor_saida
#---------------------------------------------------------------------
#                          PRODUTO ESCALAR
def produto_escalar2(vetor1,vetor2):
    '''

    :param vetor1: um dos vetores que pode ser tupla ou lista mas deve ter tamanho de dois itens, este será usado para calcular o produto escalar entre o vetor2 e ele
    :param vetor2: um dos vetores que pode ser tupla ou lista mas deve ter tamanho de dois itens, este será usado para calcular o produto escalar entre o vetor2 e ele
    :return: devolve o produto vetorial do vetor1 e vetor2
    '''
    return vetor1[0]*vetor2[0]+vetor1[1]*vetor2[1]
def produto_escalar3(vetor1,vetor2):
    '''
    :param vetor1: um dos vetores que pode ser tupla ou lista mas deve ter tamanho de dois itens, este será usado para calcular o produto escalar entre o vetor2 e ele
    :param vetor2: um dos vetores que pode ser tupla ou lista mas deve ter tamanho de dois itens, este será usado para calcular o produto escalar entre o vetor2 e ele
    :return: devolve o produto vetorial do vetor1 e vetor2
    '''
    return vetor1[0]*vetor2[0]+vetor1[1]*vetor2[1]+vetor1[2]*vetor2[2]
#---------------------------------------------------------------------
#                               NORMA
def norma2(vetor):
    '''

    :param vetor: vetor da qual será retirada a norma, deve ter como quantidade de itens 2
    :return: retorna a norma do vetor
    '''
    return math.sqrt(vetor[0]**2+vetor[1]**2)
def norma3(vetor):
    '''

    :param vetor: vetor da qual será retirada a norma, deve ter como quantidade de itens 3
    :return: retorna a norma do vetor
    '''
    return math.sqrt(vetor[0]**2+vetor[1]**2+vetor[2]**2)
#---------------------------------------------------------------------
#                        ÂNGULO ENTRE VETORES
def angulo_vetores_graus(vetor1,vetor2):
    '''

    :param vetor1: vetor que pode ter como quantidade de itens 2 ou 3
    :param vetor2: vetor que pode ter como quantidade de itens 2 ou 3
    :return: retorna o ângulo entre os dois vetores
    '''
    produto = 0
    norma_1 = None
    norma_2 = None
    if len(vetor1) == 2:
        produto = produto_escalar2(vetor1,vetor2)
        norma_1 = norma2(vetor1)
        norma_2 = norma2(vetor2)
    elif len(vetor1) == 3:
        produto = produto_escalar3(vetor1,vetor2)
        norma_1 = norma3(vetor1)
        norma_2 = norma3(vetor2)
    if norma_1*norma_2 != 0:
        return math.degrees(math.acos(produto/(norma_1*norma_2)))
    else:
        return 0
def angulo_vetores_radianos(vetor1,vetor2):
    '''

    :param vetor1: vetor que pode ter como quantidade de itens 2 ou 3
    :param vetor2: vetor que pode ter como quantidade de itens 2 ou 3
    :return: retorna o ângulo entre os dois vetores
    '''
    produto = 0
    norma_1 = None
    norma_2 = None
    if len(vetor1) == 2:
        produto = produto_escalar2(vetor1,vetor2)
        norma_1 = norma2(vetor1)
        norma_2 = norma2(vetor2)
    elif len(vetor1) == 3:
        produto = produto_escalar3(vetor1,vetor2)
        norma_1 = norma3(vetor1)
        norma_2 = norma3(vetor2)
    if norma_1 * norma_2 != 0:
        return math.degrees(math.acos(produto / (norma_1 * norma_2)))
    else:
        return 0
#---------------------------------------------------------------------
#                      CÁLCULO VETORIAL MATRICIAL
def multiplica_vetor_matriz(vetor,matriz):
    '''

    :param vetor: um vetor que pode ser tupla ou lista deve ter a mesma quantidade de itens que a largura da matriz
    :param matriz: uma matriz que pode ser de tuplas ou listas deve ter a mesma largura que a quantidade de itens do vetor
    :return: retorna o resultado da multiplicação da matriz e do vetor
    '''
    vetor_saida = []
    for i in matriz:
        soma = 0
        for pos0,j in enumerate(i):
            soma += vetor[pos0]*j
        vetor_saida.append(soma)
    return vetor_saida
#---------------------------------------------------------------------
# função para pegar o tamanho do vetor
def tamanho_vetor(vetor):
    '''

    :param vetor: o vetor da qual deseja saber o tamanho, pode ser uma tupla ou lista
    :return: retorna o tamanho do vetor
    '''
    tamanho = 0
    for i in vetor:
        tamanho += i**2
    return abs(math.sqrt(tamanho))
# função para normalizar um vetor
def normaliza_vetor(vetor):
    '''

    :param vetor: um vetor que pode ser lista ou tupla, que será normalizado e retorndado
    :return: retorna o vetor normalizado
    '''
    vetor_saida = []
    divisor = 0
    for i in vetor:
        divisor += i**2
    divisor = math.sqrt(divisor)
    for v in vetor:
        vetor_saida.append(v/divisor)
    return vetor_saida