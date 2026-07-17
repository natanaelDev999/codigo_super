n1 = float(input('escreva o preço do produto:'))
print('as opições são :dinheiro avista,cartão avista,2x no cartão e 3x no cartão')
n2 = input('escreva a forma de pagamento:').strip().capitalize()
if n2 == 'Dinheiro avista':
    n4 = (n1 * 10) / 100
    print('houve um desconto de 10% e o preço ficou R$ {:.2f}'.format(n1 - n4))
elif n2 == 'Cartão avista':
    n5 = (n1 * 5) / 100
    print('houve um desconto de 5% e o preço ficou R$ {:.2f}'.format(n1 - n5))
elif n2 == '2x no cartão':
    print('o preço ficou R$ {:.2f}'.format(n1))
elif n2 == '3x no cartão':
    n9 = (n1 * 20) / 100
    print('houve um aumento de 20% assim o preço ficou R$ {:.2f}'.format(n1 + n9))