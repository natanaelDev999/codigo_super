import socket

p = 'localhost'
port = 9700
nome = ""

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((p,port))
nome = str(input("Insira um nome como utilizador: "))
while True:
    mensagem = input('Deseja criar um artigo?: ').upper()
    if mensagem == "S":
        titulo = str(input("Insira o título do artigo: "))
        artigo = str(input("Insira o texto do artigo: "))
        socket.send((f"={nome}/{titulo}/{artigo}").encode())
        print('artigo criado e mandado ao servidor com sucesso')
    mensagem = str(input("Deseja ler um artigo?: ")).upper()
    if mensagem == "S":
        titulo = str(input("Insira o título do artigo: "))
        socket.send((f"-{titulo}").encode())
        artigo = socket.recv(1024).decode()
        print(artigo)
socket.close()
input('pressione enter para sair')