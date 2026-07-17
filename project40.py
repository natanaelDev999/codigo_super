multiplicador = 0
while True:
    n1 = int(input('escreva um numero e saiba sua tabuada:'))
    if n1 < 0:
        break
    for c in range(1,11):
        print(f'{n1} x {c} = {n1*c}')
print('progama terminado com sucesso')
