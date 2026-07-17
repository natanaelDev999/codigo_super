
n1 = float(input('diga o preço da casa R$:'))
n2 = float(input('escreva o salario do comprador:'))
n3 = int(input('escreva em quantos anos ira pagar:'))
n4 = n1 / (n3 * 12)
n5 = n2 * 30 / 100
if n4 <= n5:
    print('o emprestimo sera de R${:.2f} por mês '.format(n4))
else:
    print('não podera ser concedido {:.2f}'.format(n4))
