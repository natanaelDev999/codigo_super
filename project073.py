def voto(data):
    import datetime
    ano = datetime.date.today().year
    idade = ano - data
    if 60 > idade >= 18:
        return f'idade igual {idade} voto obrigatorio'
    elif idade < 18 and idade < 60:
        return f'idade igual {idade} voto negado'
    elif idade >= 60:
        return f'idade igual {idade} voto opcional'
dataNasci = int(input('digite seu ano de nascimento: '))
valida = voto(dataNasci)
print(valida)