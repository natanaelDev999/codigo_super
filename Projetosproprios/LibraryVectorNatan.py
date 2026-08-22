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
    vetor_saida = []
    for pos0,i in enumerate(vetor1):
        vetor_saida.append(vetor2[pos0]+i)
    return vetor_saida
# subtração de vetores
def subtrai_vetores(vetor1,vetor2):
    vetor_saida = []
    for pos0,i in enumerate(vetor1):
        vetor_saida.append(i-vetor2[pos0])
    return vetor_saida
# multiplicação de vetores
def multiplica_vetores(vetor1,vetor2):
    vetor_saida = []
    for pos0, i in enumerate(vetor1):
        vetor_saida.append(i * vetor2[pos0])
    return vetor_saida
# divisão de vetores
def divide_vetores(vetor1,vetor2):
    vetor_saida = []
    for pos0, i in enumerate(vetor1):
        vetor_saida.append(i / vetor2[pos0])
    return vetor_saida
#---------------------------------------------------------------------
#                          PRODUTO ESCALAR
def produto_escalar(vetor1,vetor2):
    return vetor1[0]*vetor2[0]+vetor1[1]*vetor2[1]
#---------------------------------------------------------------------
# função para pegar o tamanho do vetor
def tamanho_vetor(vetor):
    tamanho = 0
    for i in vetor:
        tamanho += i**2
    return abs(math.sqrt(tamanho))
# função para normalizar um vetor
def normaliza_vetor(vetor):
    vetor_saida = []
    divisor = 0
    for i in vetor:
        divisor += i**2
    divisor = math.sqrt(divisor)
    for v in vetor:
        vetor_saida.append(v/divisor)
    return vetor_saida