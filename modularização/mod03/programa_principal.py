import moeda
valor = float(input('Escreva algum valor de dinheiro: R$'))
print(f'A metade do {moeda.moeda(valor)} é {moeda.metade(valor,True)}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor,True)}')
print(f"Aumentando 10% de {moeda.moeda(valor)} o valor fica {moeda.mais(valor,10,True)}")
print(f"Diminuindo 13% de {moeda.moeda(valor)} o valor fica {moeda.menos(valor,13,True)}")
input()