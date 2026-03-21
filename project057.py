pessoas = []
pm = []
pma = []
menor = maior = 0

while True:
    nome = str(input('escreva o nome da pessoa:  '))
    peso = float(input('escreva o peso da pessoa:  '))
    pessoas.append([nome,peso])
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('deseja continuar: [S/N]  ')).upper()
    if escolha == 'N':
        break
    print('='*30)

print(f'o total de pessoa e {len(pessoas)}')
for p,l in enumerate(pessoas):
    if p == 0:
        maior = menor = l[1]
    if p > 0:
        if l[1] > maior:
            maior = l[1]
        else:
            if menor > l[1]:
                menor = l[1]

for p in pessoas:
    if p[1] == menor:
        pm.append(p[0])
    elif p[1] == maior:
        pma.append(p[0])
print(f'o menor peso e {menor} sendo os usuarios com o peso {pm}')
print(f'o maior peso e {maior} sendo os usuarios com o peso {pma}')
