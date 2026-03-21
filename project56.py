jogador = {}
# entrada de dados
nome = str(input('escreva o nome do jogador:'))
quantidade = int(input(f'escreva a quantidade de partidas jogadas por {nome}:'))
aproveitamento = []
for c in range(1,quantidade+1):
    gols = int(input(f'quantos gols na partida {c}?'))
    aproveitamento.append(gols)
# "processamento de dados"
jogador['nome'] = nome
jogador['gols'] = aproveitamento
jogador['total'] = sum(aproveitamento)
# saida de dados
print(jogador)
for c,v in jogador.items():
    print(f'{c} tem o valor de {v}')
print(f'o jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for c in range(0,len(jogador["gols"])):
    print(f' => na partida {c}, fez {jogador["gols"][c]} gols')
print(f'foi feito no total {jogador["total"]} gols')