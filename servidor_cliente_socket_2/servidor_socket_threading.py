import socket
import threading
def atender_cliente(conexao,endereco):
    dados = conexao.recv(1024)
    print(f'[SERVIDOR] relatorio: endereço do cliente: {endereco}; dados recebido: {dados.decode()} ')
    conexao.sendall('dado recebido\n'.encode())
    conexao.close()
HOST = "0.0.0.0"
PORT = 1900
socket_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_s.bind((HOST,PORT))
print('[SERVIDOR] rodando...')
socket_s.listen()
while True:
    conexao ,ender = socket_s.accept()
    print('[SERVIDOR] cliente encontrado')
    thread = threading.Thread(
        target=atender_cliente,
    args=(conexao,ender))
    daemon = True
    thread.start()