n1 = float(input('digite a primeira nota de um aluno: '))
n2 = float(input('digite sua segunda nota:'))
n3 = (n1 + n2) / 2
if n3 < 5:
    print('o aluno foi reprovado precisa \033[33mmelhorar\033[m')
elif n3 >= 5:
    print('o aluno ficara de recuperação')
elif n3 >= 7:
    print('o aluno foi aprovado')
elif n3 >= 10:
    print('o aluno foi \033[31motimo\033[m')