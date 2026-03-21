import socket
import json
import datetime
#funções
def procura_dados(dado_procura,nome2,senha2):
    dados_json = {}
    dados_encontrados = ''
    with open('dados_socket.json','r') as arquivo:
        dados_json = json.load(arquivo)
    for dado in dados_json['dados']:
        if dado_procura in dado:
            dados_encontrados += dado
            print(dado)
    dados_json['resgistros'].append(f'Registro de acesso:nome:{nome2};senha:{senha2};data de acesso{datetime.date.today()}')
    with open('dados_socket.json','w') as arquivo:
        json.dump(dados_json,arquivo)
    return dados_encontrados
def valida(proto,nome2,senha2):
    if proto == '2-1':
        dado_json = {}
        with open('usuarios_socket.json','r') as arquivo:
            dado_json = json.load(arquivo)
        achou = False
        for usuario in dado_json['usuarios']:
            if usuario[0] == nome2[3:] and usuario[1] == senha2:
                achou = True
        if achou == True:
            return 'usuarioExiste'
        else:
            return 'usuarioNãoExiste'
    else:
        dado_json2 = {}
        with open('usuarios_socket.json','r') as arquivo2:
            dado_json2 = json.load(arquivo2)
        achou = False
        for usuario in dado_json2['usuarios']:
            if usuario[0] == nome2[1:]:
                achou = True
        if achou == True:
            return 'usuarioExiste'
        else:
            return 'usuarioNãoExiste'
def arquivar_usuario(usuario):
    global resposta
    nome, senha = usuario.split(' ')
    dados_json = {}
    with open('usuarios_socket.json','r') as arquivo:
        dados_json = json.load(arquivo)
    achou = False
    for usuario in dados_json['usuarios']:
        if usuario[0] == nome[1:]:
            achou = True
    if achou == False:
        dados_json['usuarios'].append([nome[1:],senha])
        with open('usuarios_socket.json','w') as arquivo:
            json.dump(dados_json,arquivo)
        resposta = 'usuario arquivado'
    else:
        resposta = 'usuario já existe'
PORT = 6001
IP = '0.0.0.0'
socket_s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_s.bind((IP, PORT))
socket_s.listen()
print('[SERVIDOR] rodando ...')
while True:
    conexao, endereco = socket_s.accept()
    print('[SERVIDOR] conectado com sucesso a um cliente ...')
    data = conexao.recv(1024).decode()
    resposta = ''
    print(data)
    if data.startswith('1'):
        print('[SERVIDOR] dado recebido pelo cliente: ',data)
        print('[SERVIDOR] recebeu protocolo 1: ', data)
        arquivar_usuario(data)
    elif data.startswith('2-1'):
        print(data)
        protocolo = data[0:3]
        nome,dado_pesquisa,senha = data.split(' ',2)
        print(dado_pesquisa)
        valida2 = valida(protocolo,nome,senha)
        print(valida2)
        res = procura_dados(dado_pesquisa,nome,senha)
        if valida2 == 'usuarioExiste':
            resposta = f'[SERVIDOR] respondeu {valida2} e por isso você tem acesso ao nosso serviço: aqui esta sua pesquisa '+res+'\n'
        else:
            resposta = f'[SERVIDOR] respondeu {valida2},por a resposta recebida for essa você não tem acesso aos dados'
        print('[SERVIDOR] recebeu protocolo 2-1: ',data)
        valida2 = ' '
    elif data.startswith('2'):
        print(data)
        protocolo = data[0]
        nome,dado_pesquisa, senha = data.split(' ',2)
        print(dado_pesquisa)
        valida2 = valida(protocolo, nome, senha)
        print(valida2)
        res = procura_dados(dado_pesquisa,nome,senha)
        if valida2 == 'usuarioExiste':
            resposta = f'[SERVIDOR] respondeu {valida2} e por isso você tem acesso ao nosso serviço: aqui esta sua pesquisa '+res+'\n'
        else:
            resposta = f'[SERVIDOR] respondeu {valida2},por a resposta recebida for essa você não tem acesso aos dados'
        print('[SERVIDOR] recebeu protocolo 2: ',data)
        valida2 = ' '
    conexao.sendall(f'{resposta}'.encode())
    print('[SERVIDOR] serviço feito')
    conexao.close()