import socket
ip = '0.0.0.0'
port = 5000
objeto_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
objeto_s.bind((ip,port))
objeto_s.listen()
print(f'Servidor Rodando:True;\nporta:{port}')
while True:
    conexao, endereco = objeto_s.accept()
    dados = conexao.recv(1024)
    print('dados recebidos cliente conectado')
    print('dado recebido pelo cliente:',dados.decode(),'local:',endereco)
    conexao.sendall('dados recebido pelo servidor'.encode())
    conexao.close()
''''
# Cria um socket TCP usando IPv4
# AF_INET  -> tipo de endereço (IPv4)
# SOCK_STREAM -> tipo de conexão (TCP)
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define onde o servidor vai rodar
# "0.0.0.0" significa aceitar conexões de qualquer IP
# 5000 é a porta (como número de apartamento)
servidor.bind(("0.0.0.0", 5000))

# Coloca o servidor em modo de espera
# O número 5 significa que até 5 conexões podem esperar na fila
servidor.listen(5)

print("Servidor rodando...")
print("Esperando conexão na porta 5000...\n")

# Loop infinito para manter o servidor ligado
while True:
    # Espera alguém conectar
    conexao, endereco = servidor.accept()

    print(f"Conectado com: {endereco}")

    # Recebe dados do cliente (até 1024 bytes)
    dados = conexao.recv(1024)

    # Decodifica os bytes para texto
    mensagem = dados.decode()

    print("Cliente disse:", mensagem)

    # Resposta que será enviada
    resposta = "Servidor recebeu sua mensagem!"

    # Envia resposta convertendo para bytes
    conexao.send(resposta.encode())

    # Fecha a conexão com esse cliente
    conexao.close()

    print("Conexão encerrada.\n")'''