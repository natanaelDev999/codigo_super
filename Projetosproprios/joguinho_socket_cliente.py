import socket
import os
# jogo multiplayer super simples a qual se movimenta em uma matrix com outros jogadores
# demorou mais de 3 dias para ser feito
# § = você, & = outro jogador
#funções:
#le a string mandada pelo servidor
def le_string_list(string_list):
    global jogadores
    informacao = ''
    for carac in string_list:
        if not carac == '&':
            informacao += carac
        else:
            jogadores.append(informacao)
            informacao = ''
#desenha a tela
def desenha_tela():
    global tela
    global jogadores
    for y in range(len(tela)):
        for x in range(len(tela[y])):
            tela[y][x] = ' '
    tela[pos_y][pos_x] = '§'
    for regs in jogadores:
        x, y = regs.split(',')
        tela[int(y)][int(x)] = '&'
    jogadores = []
    for linha in tela:
        for coluna in linha:
            print(coluna, end=' ')
        print()

# matrix para a tela
tela = [[' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ']]

# variaveis necessarias
jogadores = []
port = "127.0.0.1"
ip = 7999
pos_x = 4
pos_y = 2

#configurações do socket
obj_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

obj_socket.connect((port,ip))

# criação do nome
nome = input('Digite seu nome: ')

#loop do jogo
while True:
    print('-'*18)
    desenha_tela()
    print('-'*18)
    #movimento do jogador
    mensagem = input('Digite um comando (quit/-- para sair): ').strip()
    if mensagem == 'w' and pos_y > 0:
        tela[pos_y][pos_x] = ' '
        pos_y -= 1
    elif mensagem == 's' and pos_y < 4:
        tela[pos_y][pos_x] = ' '
        pos_y += 1
    elif mensagem == 'd' and pos_x < 8:
        tela[pos_y][pos_x] = ' '
        pos_x += 1
    elif mensagem == 'a' and pos_x > 0:
        tela[pos_y][pos_x] = ' '
        pos_x -= 1
    # saída do jogador
    if not mensagem == 'quit/--':
        obj_socket.send((nome+';/'+str(pos_x)+';/'+str(pos_y)+'\n').encode())
    else:
        obj_socket.send((f'quit/--/;{nome}'+'\n').encode())
        break
    # trata a resposta do servidor
    resposta = obj_socket.recv(1024).decode().strip()
    resp, regsjoga = resposta.split(';/-')
    print('[CLIENTE] servidor respondeu')
    print(resp)
    le_string_list(regsjoga)
    if 'registro não pode ser feito por seu endereço não ser compatível ao do nosso banco de dados' in resp:
        nome = input('por favor escolha outro nome: ')
    # por favor verefique se seu computador utiliza o windows
    os.system('cls')
