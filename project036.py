c = False
soma = 0
soma_ = 0
print('se querer parar digite 999')
while not c:
    n1 = int(input('escreva um numero :'))
    if n1 != 999:
        soma_ += n1
        soma += 1
    else:
        print('progama finalizado')
        c = True
print('a soma dos {} e {}'.format(soma, soma_))

