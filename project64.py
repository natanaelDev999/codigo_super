from random import randint
from time import sleep
from operator import itemgetter
dic = {}
rak = {}
for c in range(1,5):
    valor = randint(0,6)
    print(f'o jogador {c} tirou {valor}')
    sleep(1)
    dic[f'jogador{c}'] = valor
rak = sorted(dic.items(), key=itemgetter(1),reverse=True)
for d,v in enumerate(rak):
    print(f'   {d+1}º lugar: {v[0]} com  {v[1]}')