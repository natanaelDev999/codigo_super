import socket

p = 'localhost'
port = 9700
nome = ""

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((p,port))
nome = str(input("\033[33mInsira um nome como utilizador:\033[33m "))
while True:
    mensagem = input('Deseja criar um \033[34martigo\033[m?: ').upper()
    if mensagem == "S":
        titulo = str(input("\033[34mInsira o título do artigo\033[m: "))
        artigo = str(input("\033[34mInsira o texto do artigo\033[m: "))
        socket.send((f"={nome}/{titulo}/{artigo}").encode())
        print('\033[34martigo criado e mandado ao servidor com sucesso\033[m')
    mensagem = str(input("\033[35mDeseja ler um artigo?\033[m: ")).upper()
    if mensagem == "S":
        titulo = str(input("\033[35mInsira o título do artigo\033[m: "))
        socket.send((f"-{titulo}").encode())
        artigo = socket.recv(1024).decode()
        print(artigo)
    cont = str(input("Deseja continuar?: ")).upper()
    if cont == "N":
        break
socket.close()
input('pressione enter para sair')