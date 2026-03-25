import socket
import threading
import json
# jogo multiplayer super simples a qual se movimenta em uma matrix com outros jogadores
# demorou mais de 3 dias para ser feito

#funções:
#elimina o registro do jogador
def elimina_registro_jogador(nome):
    dado_json = {}
    with open('jogadores_socket.json','r') as arquivo:
        dado_json = json.load(arquivo)
    print(dado_json)
    print(nome)
    for jogador in dado_json['jogadores']:
        if nome.strip() == jogador['nome'].strip():
            dado_json['jogadores'].remove(jogador)
            break
    with open('jogadores_socket.json','w') as arquivo2:
        json.dump(dado_json, arquivo2)

#registra o jogador
def registra_jogador(endereco2,nome,x,y):
    dado_json = {}
    with open('jogadores_socket.json','r') as arquivo:
        dado_json = json.load(arquivo)
    print(dado_json['jogadores'])
    if len(dado_json['jogadores']) > 0:
        achou = False
        achou_ender = False
        for jogador in dado_json['jogadores']:
            if jogador['nome'] == nome and jogador['ender'][1] == endereco2[1]:
                jogador['x'] = x
                jogador['y'] = y
                achou = True
                achou_ender = True
            elif jogador['nome'] == nome and jogador['ender'][1] != endereco2[1]:
                achou = True
                achou_ender = False
        if achou == True and achou_ender == True:
            with open('jogadores_socket.json', 'w') as arquivo2:
                json.dump(dado_json, arquivo2)
            return 'registro atualizado'
        elif achou == False and achou_ender == False:
            dado_json['jogadores'].append({'nome':nome,'ender':endereco2,'x':x,'y':y})
            print(dado_json['jogadores'])
            with open('jogadores_socket.json', 'w') as arquivo2:
                json.dump(dado_json, arquivo2)
            return 'registro feito'
        elif achou == True and achou_ender == False:
            return 'registro não pode ser feito por seu endereço não ser compatível ao do nosso banco de dados'
    else:
        dado_json['jogadores'].append({'nome':nome,'ender':endereco2,'x':x,'y':y})
        print(dado_json['jogadores'])
        with open('jogadores_socket.json', 'w') as arquivo2:
            json.dump(dado_json, arquivo2)
        return 'registro feito'
#utiliza as outras funções para responder o cliente
def trata_cliente(conexao,endereco):
    print('[SERVIDOR] cliente conectado')
    while True:
        print(endereco)
        data = conexao.recv(1024).decode()
        print(data)
        if 'quit/--'in data:
            comd, nome2 = data.split('/;')
            elimina_registro_jogador(nome2)
            break
        nome, x ,y = data.split(';/')
        respt = registra_jogador(endereco,nome,int(x),int(y))
        print('[CLIENTE] mandou ',data)
        string_list = ''
        dado_json2 = {}
        with open('jogadores_socket.json', 'r') as json_file2:
            dado_json2 = json.load(json_file2)
        for jogador in dado_json2['jogadores']:
            if jogador['nome'] != nome:
                string_list += str(jogador['x'])+','+str(jogador['y']) + '&'
        conexao.sendall(('[SERVIDOR] '+respt+';/-'+string_list+'\n').encode())
# trata do socket para a conexao
port = "127.0.0.1"
ip = 7999

ob_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ob_socket.bind((port,ip))

ob_socket.listen()
print('[SERVIDOR] rodando ...')
# loop que trata do cliente com threading
while True:
    conexao, ender = ob_socket.accept()
    thread = threading.Thread(target=trata_cliente,args=(conexao,ender,),daemon=True)
    thread.start()