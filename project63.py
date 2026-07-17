aluno = {}
nome = str(input('escreva o nome do aluno:'))
media = float(input(f'escreva a media do {nome}:'))
situacao = ' '
if media >= 7:
    situacao = 'aprovado'
elif 5 <= media < 7:
    situacao = 'recuperação'
else:
    situacao = 'reprovado'
aluno['nome'] = nome
aluno['media'] = media
aluno['situação'] = situacao
for i,v in aluno.items():
    print(f'{i} e igual a {v}')
