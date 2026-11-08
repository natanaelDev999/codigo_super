#---------------------------------------------------------------------
#                         LIBRARYVECTORNATAN
#---------------------------------------------------------------------
#                            BIBLIOTECAS
import math
from decimal import Decimal
#---------------------------------------------------------------------
# biblioteca para manipulação de vetores
#---------------------------------------------------------------------
#                        OPERAÇÕES MATEMÁTICAS
#---------------------------------------------------------------------
# potência de vetores
def potencia_vetores(vetor1,elevacao: int):
    vetor_saida = []
    for c in vetor1:
        vetor_saida.append(c**elevacao)
    return vetor_saida
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
        if vetor2[pos0] != 0:
            vetor_saida.append(i / vetor2[pos0])
        else:
            vetor_saida.append(1)
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
        return math.acos(produto / (norma_1 * norma_2))
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
def multiplica_matriz_matriz(matriz1,matriz2):
    '''

    :param matriz1: Pode ser uma matriz de tuplas ou listas, e pode ser 4x4 ,3x3 ...
    :param matriz2: Pode ser uma matriz de tuplas ou listas, e pode ser 4x4 ,3x3 ...
    :return: retorna a matriz resultante da multiplicação de matriz1 e matriz2
    '''
    matriz_saida = []
    # achei o algoritmo da wikipedia ,link: https://pt.wikipedia.org/wiki/Algoritmo_de_multiplica%C3%A7%C3%A3o_de_matrizes
    for i in range(0,len(matriz1)):
        vetor_adicional = []
        for j in range(0,len(matriz2[0])):
            soma = 0
            for k in range(0,len(matriz1[0])):
                soma = soma + matriz1[i][k]*matriz2[k][j]
            vetor_adicional.append(soma)
        matriz_saida.append(vetor_adicional)
    return matriz_saida

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
#---------------------------------------------------------------------
# função para preencher um vetor com um valor
def preenche_vetor(valor,quantidade:int):
    vetor_saida = []
    for c in range(quantidade+1):
        vetor_saida.append(valor)
    return vetor_saida
#---------------------------------------------------------------------
#                            QUATERNIONS
# função para soma de quaternions
def soma_quaternions(q1,q2):
    '''

    :param q1: Deve ser uma lista quadridimensional
    :param q2: Deve ser uma lista quadridimensional
    :return: retorna a soma dos dois quaternions
    '''
    q_saida = []
    for pos0,c in enumerate(q1):
        q_saida.append(float(Decimal(str(c))+Decimal(str(q2[pos0]))))
    return q_saida
# função para multiplicação de escalar por quaternions
def multiplica_escalar_quaternion(escalar: float,q1):
    '''

    :param escalar: valor escalar
    :param q1:  Deve ser uma lista quadridimensional
    :return: retorna o quaternion resultante da multiplicação do escalar e do quaternion
    '''
    q_saida = []
    for c in q1:
        q_saida.append(float(Decimal(str(escalar))*Decimal(str(c))))
    return q_saida
# função para conjugação de quaternions
def conjuga_quaternion(q1):
    '''

    :param q1: Deve ser uma lista quadridimensional
    :return: retorna o quaternion conjugado
    '''
    return [q1[0],q1[1]*-1,q1[2]*-1,q1[3]*-1]
# função para norma de quaternions
def norma_quaternion(q1):
    '''

    :param q1:  Deve ser uma lista quadridimensional
    :return: retorna a norma do quaternion
    '''
    vetor_saida = []
    divisor = 0
    for i in q1:
        divisor += i ** 2
    divisor = math.sqrt(divisor)
    for v in q1:
        vetor_saida.append(v / divisor)
    return vetor_saida
# função para multiplicar quaternions
def multiplica_quaternions(q1,q2):
    '''

    :param q1:  Deve ser uma lista quadridimensional
    :param q2:  Deve ser uma lista quadridimensional
    :return: retorna o quaternion resultante da multiplicação de q1 e q2
    '''
    return [q1[0]*q2[0]- q1[1]*q2[1]- q1[2]*q2[2]- q1[3]*q2[3],
               q1[0]*q2[1]+ q2[0]*q1[1]+ q1[2]*q2[3]- q1[3]*q2[2],
               q1[0]*q2[1]+ q2[0]*q1[2]+ q1[3]*q2[1]- q1[1]*q2[3],
               q1[0]*q2[3]+ q2[0]*q1[2]+ q1[1]*q2[2]- q1[2]*q2[1]]
