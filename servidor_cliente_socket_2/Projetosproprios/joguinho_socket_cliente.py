import socket

tela = [[' ',' ',' ',' ',' ',' ',' ',' ','*'],
        [' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' '],
        ['*',' ',' ',' ',' ',' ',' ',' ',' '],]
def desenhar_tela(posx,posy):
    global tela
    tela[posx][posy] = '§'
    for linha in tela:
        for coluna in linha:
            print(coluna,end=' ')
        print()
pos_x = 4
pos_y = 2
port = "127.0.0.1"
ip = 7999

obj_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

obj_socket.connect((port,ip))

desenhar_tela(pos_x,pos_y)
while True:

    resposta = obj_socket.recv(1024)

    mensagem = input('escreva uma mensagem(/quit para sair): ')

    if mensagem == '/quit':
        break

    obj_socket.send(mensagem.encode())

    resposta = obj_socket.recv(1024).decode()

    print('[CLIENTE] servidor respondeu')
    print(resposta)
