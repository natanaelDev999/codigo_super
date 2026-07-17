import random
import time
print('vamos jogar pedra papel tesoura')
n1 = 'tesoura'
n5 = 'pedra'
n3 = 'papel'
n2 = random.choice([n1, n5 , n3 ])
n6 = input('digite sua escolha:')
print('\033[31mprossecando ...\033[m')
time.sleep(3)
if n2 == n6:
    print('{} {} empatou'.format(n6, n2))
elif n2 == n6:
    print('{} {} empatou'.format(n6, n2))
elif n2 == n6:
    print('{} {} empatou'.format(n6, n2))
elif n2 == n1 and n6 == 'papel':
    print('\033[4;31m{} {} ganhei !!!:)\033[m'.format(n6, n2))
elif n2 == n1 and n6 == 'pedra':
    print('{} {} você ganhou !!!'.format(n6, n2))
elif n2 == n5 and n6 == 'papel':
    print('{} {} você ganhou !!!'.format(n6, n2))
elif n2 == n3 and n6 == 'tesoura':
    print('{} {} você ganhou'.format(n6, n2))
elif n2 == n3 and n6 == 'pedra':
    print('\033[4;31m{} {} ganhei !!!\033[m'.format(n6, n2))
elif n2 == n5 and n6 == 'tesoura':
    print('\033[4;31m{} {} ganhei\033[m'.format(n6, n2))