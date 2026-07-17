p1 = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez')
p2 = ('onze','doze','treze','catorze','quinze','desesseis','desessete','dezoito','dezenove','vinte')
n = p1 + p2
while True:
    escolha = -1
    while escolha > 20 or escolha < 0:
        print('tente novamente',end = ' ')
        escolha = int(input('escreva um numero de 0 a 20:'))
    p = ' '
    n1 = 0
    while True:
        if escolha == n1:
            p = n[n1]
            break
        n1 += 1
    print(f'o numero digitado foi {p}')
    escolha2 = ' '
    while escolha2 not in 'SN':
        escolha2 = str(input('deseja continuar: [S/N]')).upper().strip()[0]
    if escolha2 == 'N':
        break
