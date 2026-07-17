alunos = []
while True:
    nome = str(input('escreva o nome do aluno: '))
    nota1 = float(input('escreva a primeira nota do aluno: '))
    nota2 = float(input('escreva a segunda nota do aluno: '))
    media = (nota1 + nota2)/2
    alunos.append([nome,nota1,nota2,media])
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('deseja continuar: [S/N]')).strip().upper()[0]
    if escolha ==  'N':
        break
print('=-'*15,'BOLETIM DE NOTAS','=-'*15)
print('No. NOME      MEDIA')
cont = 0
print('-'*30)
for a in alunos:
    print(f'{cont: <4}{a[0]: <10}{a[3]: <15}')
    cont += 1
while True:
    print('-'*30)
    escolha = int(input('deseja ver as notas de qual aluno? (999 interrompe): '))
    if not escolha == 999 and escolha <= len(alunos)-1:
        print(f'as nota de {alunos[escolha][0]} são {alunos[escolha][1:3]}')
    else:
        print('finalizando...')
        break