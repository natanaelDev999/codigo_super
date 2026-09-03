import socket
import json
import threading

lock = threading.Lock()

def salva_artigo(titulo,artigo,autor):
    global lock
    dados = {}
    with lock:
        with open("artigos.json",'r') as arquivo:
            dados = json.load(arquivo)
    dados["artigos"].append([titulo,autor,artigo])
    with lock:
        with open("artigos.json",'w') as arquivo2:
            json.dump(dados,arquivo2)

def ler_artigo(titulo):
    global lock
    print(lock)
    dados = {}
    artigo_retorna = []
    with lock:
        with open("artigos.json",'r') as arquivo:
            dados = json.load(arquivo)

    for artigo in dados["artigos"]:
        if artigo[0] == titulo:
            artigo_retorna = artigo
    return artigo_retorna

def trata_cliente(conexao,ender):
    global lock
    print('[SERVIDOR] cliente encontrado')
    while True:
        dados = conexao.recv(1024).decode()
        print(dados)
        if dados[0] == "=":
            autor, titulo, artigo = dados[1:].split("/")
            salva_artigo(titulo,artigo,autor)
            print('[SERVIDOR] artigo criado')
        elif dados[0] == "-":
            dados = dados[1:]
            artigo = ler_artigo(dados)
            conexao.sendall((f"Titulo:{artigo[0]}\nAutor:{artigo[1]}\n{artigo[2]}").encode())

    conexao.close()

ip = "0.0.0.0"
port = 9700

objeto_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
objeto_s.bind((ip,port))
objeto_s.listen()

print(f'Servidor Rodando:True;\nporta:{port}')
while True:
    conexao, endereco = objeto_s.accept()

    thread = threading.Thread(target=trata_cliente, args=(conexao, endereco,))

    thread.start()