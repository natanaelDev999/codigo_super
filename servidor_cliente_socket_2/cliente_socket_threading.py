import socket
HOST = 'localhost'
ip = 1900
socket_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_s.connect((HOST, ip))
mensagem = input('escreva algo: ')
socket_s.send((mensagem+'\n').encode())
print('mensagem direcionada para o servidor')
resposta = socket_s.recv(1024).decode()
print('[SERVIDOR] respondeu: ',resposta)
socket_s.close()