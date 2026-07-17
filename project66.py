pessoas = []
media = 0
while True:
    # entrada de dados
    nome = str(input('digite o nome da pessoa:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('digite o sexo da pessoa:')).upper()
        if sexo not in 'MF':
            print('por favor, digite apenas M ou F')
    idade = int(input('digite a idade da pessoa:'))
    media += idade
    #processamento de dados
    pessoas.append({'nome':nome,'idade':idade,'sexo':sexo})
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('deseja continuar o cadastro:')).upper()
        if escolha not in 'SN':
            print('erro: por favor, digite apenas S ou N')
    if escolha == 'N':
        break
print('=-'*30)
# saida de dados
print(f'o total de pessoas cadastradas é {len(pessoas)}')
print(f'a media de idade é {media/len(pessoas):.1f} anos')
mulheres = []
for c in pessoas:
    if  c['sexo'] == 'F':
        mulheres.append(c['nome'])
print(f'as mulheres cadastradas foram {mulheres}')
acima_peso = []
for c in  pessoas:
    if c['idade'] > media/len(pessoas):
        acima_peso.append(c)
print(f'as pessoas acima da media de idade é {acima_peso}')
for c in acima_peso:
    for v,s in c.items():
        print(f'{v} = {s};',end=' ')
    print()
