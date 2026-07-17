import time
def main(mens):
    titulo(f'PROCURANDO O COMANDO OU BIBLIOTECA {mens}','44')
    time.sleep(1)
    help(mens)

def titulo(mensg,cor):
    tam = len(mensg) + 2
    print(f'\033[0;30;{cor}m',end='')
    print('~'*(tam+1))
    print(f' {mensg}')
    print('~'*tam)
    print('\033[m')

com = ''
while True:
    titulo('SISTEMA DE AJUDA PyHelp','42')
    com = input('Pesquise uma função ou biblioteca: ')
    if com == 'fim':
        break
    else:
        main(com)
titulo('ATÉ LOGO','41')