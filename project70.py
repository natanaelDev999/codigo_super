from time import sleep
def contador(i,d,p):
    print('-'*30)
    if p == 0:
        p = 1
    print(f'contagem de {i} ate {d} de {p} em {p}')
    if i < d:
        if p < 0:
            p = abs(p)
        for c in range(i,d+1,p):
            print(c,end=' ')
            sleep(0.4)
        print('FIM')
    else:
        for c in range(i,d-1,-abs(p)):
            print(c,end=' ')
            sleep(0.4)
        print('FIM')
contador(0,10,1)
contador(10,0,2)
i = int(input('inicio:'))
d = int(input('fim:'))
p = int(input('passo:'))
contador(i,d,p)