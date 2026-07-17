total = maior1000 = quant = menor = preco_ = 0
while True:
    nome = str(input('digite o nome do produto:'))
    preco = float(input('qual o preço do produto:R$'))
    quant += 1
    total += preco
    if preco > 1000:
        maior1000 += 1
    if quant == 1:
        menor = nome
        preco_ = preco
    if quant >= 2:
        if preco < preco_:
            menor = nome
            preco_ = preco
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('que continuar?: S/N')).upper().strip()
    if escolha == 'N':
        break
print(f'o total foi R${total:.2f}\na compra teve {maior1000} produtos com preços superiores a 1000\no nome do menor preço e {menor}')

