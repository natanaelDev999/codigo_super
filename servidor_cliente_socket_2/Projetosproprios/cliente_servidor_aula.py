import socket
p = 'localhost'
port = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((p,port))
mensagem = input('qual a mensagem que deseja comunicar:  ')
s.send(mensagem.encode())
print('mensegem comunicada')
resposta = s.recv(1024)
print('resposta do servidor:',resposta.decode())
s.close()
'''
# Cria socket TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
# "localhost" significa o próprio computador
# 5000 deve ser a mesma porta do servidor
cliente.connect(("localhost", 5000))

# Mensagem que será enviada
mensagem = input("Digite uma mensagem para o servidor: ")

# Envia mensagem convertendo para bytes
cliente.send(mensagem.encode())

# Recebe resposta do servidor
resposta = cliente.recv(1024)

# Mostra resposta convertida para texto
print("Servidor respondeu:", resposta.decode())

# Fecha conexão
cliente.close()'''