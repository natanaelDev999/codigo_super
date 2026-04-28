import moeda
valor = float(input('Escreva algum valor de dinheiro: R$'))
print(f'A metade do {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f"Aumentando 10% de {moeda.moeda(valor)} o valor fica {moeda.moeda(moeda.mais(valor,10))}")
print(f"Diminuindo 13% de {moeda.moeda(valor)} o valor fica {moeda.moeda(moeda.menos(valor,13))}")
input()