import time
def maior(*num):
    maior = 0
    for i,o in enumerate(num):
        if i == 0:
            maior = o
        else:
            if o > maior:
                maior = o
    print('Analisando os dados')
    for o in num:
        print(o,end=' ')
        time.sleep(0.5)
    print(f'Foram informados {len(num)} numeros ao todo')
    print(f'o maior dos numeros é {maior}')
maior(2,5,2,6,3,1)

