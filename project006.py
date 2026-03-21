n1 = int(input('escreva quantos km o carro andou:'))
if n1 <= 80:
    print('otimo não ira ganhar multa :)')
else:
    n2 = (n1 - 80)*7
    print('esta fora da velocidade permitida que e km80 ira ganhar uma multa de R${:.2f}'.format(n2))

