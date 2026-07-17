pessoa1 = {}
nome = str(input('escreva seu nome:'))
ano = int(input('escreva o ano de seu nascimento:'))
ct = int(input('escreva o valor da carteira de trabalho (0 não tem) :'))
idade = 2025 - ano
pessoa1['nome'] = nome
pessoa1['idade'] = idade
pessoa1['ctps'] = ct
if ct != 0:
    ano_contra = int(input('escreva o ano de contratação:'))
    salario = float(input('escreva o salario que recebe:'))
    aposentadoria_ano = ano_contra + 35
    idade_aposentadoria = aposentadoria_ano - ano
    pessoa1['contratação'] = ano_contra
    pessoa1['salario'] = salario
    pessoa1['aposentadoria'] = idade_aposentadoria
for c,v in pessoa1.items():
    print(f'{c} tem valor de {v}')

