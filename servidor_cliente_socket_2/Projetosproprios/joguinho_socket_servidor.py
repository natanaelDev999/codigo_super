import socket
import threading

def trata_cliente(conexao):
    while True:
        print('[SERVIDOR] cliente conectado')
        conexao.sendall(('protofim'+'\n').encode())
        mensagem = conexao.recv(1024).decode()
        if not mensagem:
            break
        print('[CLIENTE] mandou: ',mensagem)
        conexao.sendall(('[SERVIDOR] recebeu: '+ mensagem+'\n').encode())
    conexao.close()

port = "127.0.0.1"
ip = 7999

ob_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ob_socket.bind((port,ip))

ob_socket.listen()
print('[SERVIDOR] rodando ...')
while True:
    conexao, ender = ob_socket.accept()
    thread = threading.Thread(target=trata_cliente,args=(conexao,),daemon=True)
    thread.start()