quant = soma = 0
while True:
    n1 = int(input('digite um numero(999 pra parar): '))
    if n1 == 999:
        break
    soma += n1
    quant += 1
print(f'a soma dos {quant} e {soma}')