import socket
import threading
import json

lock = threading.Lock()

def lista_cont(nome):
    dado_json = {}
    list = []
    with lock:
        with open('Usuarios_Tel-mail.json','r') as arquivo:
            dado_json = json.load(arquivo)
    for pos,usuario in enumerate(dado_json['usuarios']):
        if usuario['nome'] == nome:
            del dado_json['usuarios'][pos]
        else:
            list.append(usuario['nome'])
    return list

def valida(nome,ender):
    dado_json = {}
    with lock:
        with open('Usuarios_Tel-mail.json','r') as arquivo:
            dado_json = json.load(arquivo)

    if 0 < len(dado_json['usuarios']):
        achou_nome = False
        achou_ender = False
        for usuario in dado_json['usuarios']:
            if usuario['nome'] == nome and usuario['ender'][1] == ender[1]:
                achou_nome = True
                achou_ender = True
            elif usuario['nome'] == nome and usuario['ender'][1] != ender[1]:
                achou_nome = True
                achou_ender = False
        if achou_nome == False and achou_ender == False:
            dado_json['usuarios'].append({'nome':nome,'ender':ender})
            with lock:
                with open('Usuarios_Tel-mail.json', 'w') as arquivo2:
                    json.dump(dado_json, arquivo2)
            return 'registro de usuario feito'
        elif achou_nome == True and achou_ender == True:
            return 'registro encontrado'
        elif achou_nome == True and achou_ender == False:
            return 'registro não compatível'
    else:
        dado_json['usuarios'].append({'nome': nome, 'ender': ender})
        with lock:
            with open('Usuarios_Tel-mail.json', 'w') as arquivo2:
                json.dump(dado_json, arquivo2)
        return 'registro de usuario feito'
def main(con,ender):
    print('[SERVIDOR] cliente conectado')
    while True:
        data = con.recv(1024).decode()
        para, email, nome = data.split('/')
        print(nome)
        if email in 'exit-':
            break
        resps = valida(nome,ender)
        resps_cliente = []
        if resps == 'registro de usuario feito':
            for email2 in mensagens:
                if email2['para'] == nome:
                    resps_cliente.append('para:' + email2['para'] + ';email:' + email2['email'] + ';de:' + email2['de'])
                    mensagens.remove(email2)
            if not  'Contects--' in email:
                mensagens.append({'para':para,'email':email,'de':nome})
            print(mensagens)
        #
        elif resps == 'registro encontrado':
            for email2 in mensagens:
                if email2['para'] == nome:
                    resps_cliente.append('para:' + email2['para'] + ';email:' + email2['email'] + ';de:' + email2['de'])
                    mensagens.remove(email2)
            if not 'Contects--' in email:
                mensagens.append({'para': para, 'email': email, 'de': nome})
            print(mensagens)
        print(data)
        if 'Contects--' in email:
            resp = lista_cont(nome)
            resps_cliente = str(resp)[1:-1]
        con.sendall((resps+';Tel-mails:\n'+'\033[35m'+str(resps_cliente)[1:-1]+'\033[m').encode())
    con.close()

mensagens = []
obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

obj.bind(('0.0.0.0',7900))

obj.listen()
print('[SERVIDOR] rodando ...')

while True:
    conexao , end = obj.accept()

    thread = threading.Thread(target=main,args=(conexao,end,))

    thread.start()