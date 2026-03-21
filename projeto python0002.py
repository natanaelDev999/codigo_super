n1 = int(input('escreva um salario:'))
if n1  >= 1250:
    n2 = (n1*10) / 100
    print('por ser  maior que R$1200.00 houve um aumento de 10% que ficou R${:.2f} '.format(  n1 + n2 ))
else:
    n3 = (n1*15) / 100
    print('por ser menor que R$1200.00 houve um aumento de 15% que ficou R${:.2f}'.format( n1 + n3 ))