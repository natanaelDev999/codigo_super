def ficha(nome='<desconhecido>',gols=0):
    return f'o jogador do nome {nome} fez {gols} gol(s)'
nome2 = input('qual o nome do jogador: ')
gols2 = input('quantos gols ele fez: ')
if gols2.isnumeric() == True:
    gols2 = int(gols2)
else:
    print('escreva em forma de numero')
print(ficha(nome2,gols2))