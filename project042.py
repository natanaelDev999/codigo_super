n = 1
mais18 = 0
quantm = 0
mmenor20 = 0
while True:
    print(f'cadastre a {n} pessoa ')
    idade = int(input(f'digite a idade da {n} pessoa:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input(f'digite o sexo [M/F] de {n} pessoa:')).upper().strip()[0]
    n += 1
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        quantm += 1
    if sexo == 'F' and idade < 20:
        mmenor20 += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('quer continuar o cadastramento?: [S/N]')).upper().strip()[0]
    if escolha == 'N':
        break
print(f'o cadastro teve o total de {mais18} maiores que 18\nao todo houve {quantm} homens cadastrados\ne tivemos {mmenor20} mulheres menores de 20 ')

