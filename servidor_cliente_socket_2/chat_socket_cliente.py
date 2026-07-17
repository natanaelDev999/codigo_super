import socket
import time
import datetime
import json
def retira_registro(nome_usuario_2):
    dado_json = {}
    with open('usuarios.json','r') as arquivo:
        dado_json = json.load(arquivo)
    for usuario in dado_json['usuarios']:
        if usuario == nome_usuario_2:
            dado_json['usuarios'].remove(usuario)
    with open('usuarios.json','w') as arquivo2:
        json.dump(dado_json, arquivo2)
def valida_nome(nome_usuario):
    dado_json = {}
    with open('usuarios.json','r') as arquivo:
        dado_json = json.load(arquivo)
    achou = False
    for usuario in dado_json['usuarios']:
        if usuario == nome_usuario:
            achou = True
    if achou == False:
        dado_json['usuarios'].append(nome_usuario)
        with open('usuarios.json','w') as arquivo:
            json.dump(dado_json, arquivo)
    else:
        return '\033[31mO nome já existe!Escolha outro.\033[m'
def time_sleep():
    time.sleep(0.87)
def mostra_logo():
    print('\033[34m  ___\033[m                     \033[34m    | |  \033[m   ')
    time_sleep()
    print(' \033[34m| |\033[m   | |  | |    /| |   \033[34m--- |----\033[m   |---    | |')
    time_sleep()
    print('\033[34m | |\033[m   |____| |   /__| |  \033[34m    | |  \033[m   |       | |')
    time_sleep()
    print(' \033[34m| |\033[m   | |  | |  /    | |  \033[34m   | | \033[m    |---    | |')
    time_sleep()
    print('\033[34m  ___ \033[m | |  | | /      | | \033[34m   | |   \033[m  |____   |____')
    time_sleep()
    print('\n99% por favor espere, para mandar suas mensagens')
    for c in range(0,3):
        time_sleep()
    print()
    print('CHATEL;Criador:Natanael Trajano Dos Reis')
host = '192.168.0.218'
ip = 3800
socket_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_s.connect((host, ip))
mostra_logo()
print('\033[33mpor ser um chat arcaico se estiver na validação de quer continuar a mandar mensagens,por favor somente aperte enter para visualizar o que foi comunicado (se acha que a resposta)\033[m')
nome = ' '
cert = False
for cont in range(0,3):
    nome = input('crie um nome: ').strip()
    resul = valida_nome(nome)
    if resul == None:
        cert = True
        break
    else:
        print(resul)
if cert == True:
    while True:
        mensagem = input('Digite algo: ')
        chat = socket_s.recv(4000).decode()
        print('\033[36mchat\033[m: ',chat)
        print('\033[34m-\033[m'*30)
        socket_s.send((mensagem+f'|\033[34mDe\033[m:{nome};\033[35mdata\033[m/\033[33mhora\033[m:{datetime.datetime.now().date()},{datetime.datetime.now().time().hour}:{datetime.datetime.now().time().minute}\n').encode())
        chat_atul = socket_s.recv(4000).decode()
        print('\033[36mchat\033[m:',chat_atul)
        print('\033[34m-\033[m'*30)
        resp = ' '
        while not resp in ['S','N']:
            resp = input('Deseja continuar a mandar mensagens? [\033[33mS\033[m/\033[31mN\033[m]: ').upper().strip()
        if resp == 'N':
            retira_registro(nome)
            break
else:
    print('\033[31mDesculpe mas o bloqueamos por tantas tentativas de utilizar um nome ja existente!\033[m')