def ficha(nome='<desconhecido>',gols=0):
    print(f'O nome do jogador é {nome}, a quantidade de gols feita pelo jogador é {gols}')

nome = str(input("Nome do jogador: "))
gols = str(input("Quantos gols foram feitos: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome,gols)