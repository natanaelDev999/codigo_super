import moeda
valor = float(input('Escreva algum valor de dinheiro: R$'))
print(f'A metade do {valor} é {moeda.metade(valor)}')
print(f'O dobro de {valor} é {moeda.dobro(valor)}')
print(f"Aumentando 10% de {valor} o valor fica {moeda.mais(valor,10):.1f}")
print(f"Diminuindo 13% de {valor} o valor fica {moeda.menos(valor,13):.1f}")
input()