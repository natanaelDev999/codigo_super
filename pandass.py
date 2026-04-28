import time
import random
def m1():
    print("-=    Calculadora de x    =-")
    valor_igual = int(input('Qual valor será igual a multiplicação: '))
    print(f"{valor_igual} = ? . ?")
    valor_descoberto = int(input('Qual o primeiro fator o que se sabe o valor: '))
    print(f"{valor_igual} = {valor_descoberto} . x")
    print(f"=-   Calculando o valor de x ",end=' ')
    for c in range(0,3):
        time.sleep(1)
        print('.', end=' ')
    print('   -=')
    if valor_descoberto < valor_igual:
        print(f"   O valor de x é {valor_igual / valor_descoberto}")
    else:
        print(f"   O valor de x é {valor_descoberto / valor_igual}")
def m2():
    x = 4
    print("-=    Calculadora de dano    =-")
    for c in range(0, 20):
        valor_igual = random.randint(1,20)
        valor_descoberto = random.randint(1, 20)
        print(f"A força foi {valor_descoberto}, o dano foi {valor_descoberto*x}")
m2()