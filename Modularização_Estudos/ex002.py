from modulos import moeda

v = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(v,True)} é {moeda.moeda(moeda.metade(v),True)}')
print(f'O dobro de {moeda.moeda(v,True)} é {moeda.moeda(moeda.dobro(v),True)}')
print(f'Aumentado 10%, temos {moeda.moeda(moeda.aumentar(v, 10),True)}')
print(f'Diminuindo 13% temos {moeda.moeda(moeda.diminuir(v, 13),True)}')