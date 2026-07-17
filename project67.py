jogadores = []
while True:
    nome = str(input('escreva o nome do jogador:'))
    quantidade = int(input(f'escreva a quantidade de partidas jogadas por {nome}:'))
    aproveitamento = []
    for c in range(1,quantidade+1):
        gols = int(input(f'quantos gols na partida {c}?'))
        aproveitamento.append(gols)
    jogadores.append({'nome':nome,'gols':aproveitamento,'total':sum(aproveitamento)})
    escolha =  ' '
    while escolha not in 'NS':
        escolha = str(input('deseja continuar a analise:')).upper()
    if escolha == 'N':
        break
print(f'cod {"nome": <10}{"gols": <10}{"total"}')
for v,j in enumerate(jogadores):
    print(f'{v} {j["nome"]: <10}  {str(j["gols"]): <13}{j["total"] }')
while True:
    escolha = int(input('Deseja mostrar dados da qual jogador?: (999 para parar)'))
    if escolha != 999:
        if escolha <= len(jogadores) - 1:
            print(f'--LEVANTAMENTO DO JOGADOR {jogadores[escolha]['nome']}')
            for g,j in enumerate(jogadores[escolha]['gols']):
                print(f' No jogo {g+1} fez {j} gols')
        else:
            print(f'ERRO: Não existe jogador com indice {escolha}')
    else:
        break




