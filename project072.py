import random as r
numeros = []
def sorteio(list):
    for c in range(0,5):
        list.append(r.randint(0,10))
    print('sorteando 5 valores da lista:',end=' ')
    for o in list:
        print(o,end=' ',flush=True)
    print('PRONTO!')
def somp(list):
    pares = 0
    for o in list:
        if o % 2 == 0:
            pares += o
    print(f'Somando os valores pares de {list}, temos {pares}')
sorteio(numeros)
somp(numeros)
