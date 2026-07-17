from datetime import date
soma = 0
soma_ = 0
for c in range(7):
    data = date.today().year
    n1 = int(input('escreva a data de nascimento de alguem'))
    n = data - n1
    if n >= 21:
        soma += 1
    else:
        soma_ += 1
print('das sete pessoas {} estão na maioridade e {} não estão na maioridade'.format(soma, soma_))

