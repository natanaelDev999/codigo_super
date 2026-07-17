n1 = int(input('digite a quantidade de km que tem uma viagem de avião de 100 e mais:'))
if n1  <= 200:
    n2 = n1*0.50
    print('o preço dessa  viagem se um km e R$0.50 e R${:.2f}'.format(n2))
else:
    n3 = n1*0.45
    print('o preço dessa viagem se um km e R$0.45 e R${:.2f}'.format(n3))
