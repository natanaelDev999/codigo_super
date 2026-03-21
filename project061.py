import random
import time
print('=-'*20)
print('             MEGA SENA               ')
print('=-'*20)
lista = []
num = int(input('quantos jogos quer que eu sorteie? '))
for c in range(0,num):
    quant = []
    for v in range(0,6):
        nums = random.randint(1,60)
        quant.append(nums)
    lista.append(quant)
print(f'=-=-= SONTEANDO {num} JOGOS =-=-=')
for c in range(0,num):
    print(f'jogo {c + 1}: {lista[c]}')
    time.sleep(0.5)