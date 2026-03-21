import socket
import threading
import time
chat = []
text_chat = ''
def tratar_cliente(conexao):
    global chat
    global text_chat
    for mens in chat:
        text_chat += '-' + mens
    while True:
        print(chat)
        print('cliente conectado')
        conexao.sendall((str(text_chat)+'\n').encode())
        data = conexao.recv(4500).decode()
        if not data:
            break
        print(data)
        chat.append(data)
        time.sleep(1)
        text_chat += f'\033[31m-\033[m{data}'
        time.sleep(1)
        conexao.sendall((str(text_chat)+'\n').encode())
        print('mensagem recebida')
    conexao.close()
port = '192.168.0.218'
ip = 3800
mensagens = []
socket_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_s.bind((port, ip))
socket_s.listen()
print('\033[32mA estrutura para analise de mensagens e feita analisando aonde aparece (cliente conectado) que sera o começo da interação que somente manda um unica mensagem neste e sera fechado com (mensagem recebida) ou seja a mensagem comunicada\033[m')
print('[SERVIDOR] servidor rodando ...')
while True:
    conexao, ender = socket_s.accept()
    thread = threading.Thread(target=tratar_cliente,args=(conexao,),daemon=True)
    thread.start()
