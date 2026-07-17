import socket

emails = []
tela = [[' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ']]
def trata_img(pos,string):
    cont = ''
    achou = False
    for obj in string[pos:]:
        if obj != '¢' and achou == False:
            cont += obj
        else:
            achou = True
    cod = []
    achouu = False
    for c in cont:
        if c == '<':
            achouu = True
        elif c == '>':
            achouu = False
        elif achouu == True and c.isnumeric():
            cod.append(c)
    for c in range(0,len(cod),2):
        tela[int(cod[c])][int(cod[c+1])] = '\033[0;34;44m#\033[m'
        # print(f'cod: {cod[c],cod[c+1]}')
    desenha_tela(True)
def desenha_tela(clear=False):
    for linha in tela:
        for coluna in linha:
            print(coluna,end=' ')
        print()
    # pegando a posição há mais garantia de mudança
    if clear == True:
        for pos,linha in enumerate(tela):
            tela[pos] = [' ',' ',' ',' ',' ',' ']

def img():
    cod = []
    desenha_tela()
    while True:
        y = int(input("Escreva a coordenada y do pixel: "))
        x = int(input("Escreva a coordenada x do pixel(999 para parar): "))
        if x == 999 or y == 999:
            break
        elif x <= 5 and y <= 5 and x >= 0 and y >= 0:
            cod.append(f'<{y} {x}>')
        else:
            print("\033[31mAlgum dado não corresponde ao nosso protocolo\033[m")
    for cods in cod:
        tela[int(cods[1])][int(cods[3])] = '\033[0;34;44m#\033[m'
    desenha_tela(True)
    cod_string = ''
    for iten in cod:
        cod_string += str(iten)
    return cod_string
def trata_string(string):
    email = ''
    print(string)
    for pos,ms in enumerate(string[0:]):
        if ms == '¢':
            trata_img(pos+1,string)
            break
        if ms == '§' and string[pos+1] == '-':
            email += ms + string[pos+1]
            emails.append(email)
            email = ''
        else:
            email += ms
    emails.append(email)
def desenha_email():
    global emails
    for pos, email in enumerate(emails):
        print(f'{pos})\n{email}\n')
    emails = []
obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

obj.connect(('localhost',7900))
nome = ''
while not '@' in nome:
    nome = input('Crie um endereço de \033[34mTel-mail\033[m: ')
    if not '@' in nome:
        print('\033[31mDesculpa mas o endereço tem que ter um @\033[m')
print('Se deseja ver os contatos de outras pessoas utilize o comando \033[33mContects--\033[m')
while True:
    para = input('Para: ')
    print('\033[34m-'*20,'\033[m')
    assunto = input('Assunto: ')
    tipo = input("Qual o tipo de Tel-mail deseja utilizar: (img para imagem ou txt para texto(que serve para comandos)) ")
    if tipo == 'txt':
        email = input('Tel-mail(exit- para sair): ')
        if 'exit-' in email:
            obj.send((para+'/'+'assunto: '+assunto+'    '+'exit-'+'/'+nome).encode())
            break
        obj.send((para+'/'+'assunto: '+assunto+'    '+email+'/'+nome).encode())
        resp = obj.recv(1024).decode()
        if 'registro não compatível' in resp:
            print('\033[31mDesculpe mas a resposta do Servidor nos comunicou que seu endereço de Tel-mail e incompatível\033[m ')
            nome = input('Refaça se endereço de Tel-mail: ')
        else:
            trata_string(str(resp))
            desenha_email()
            print('\033[m')
    elif tipo == 'img':
        email = img()
        obj.send((para+'/'+'assunto: '+assunto+'    img¢'+email+'¢'+'/'+nome).encode())
        resp = obj.recv(1024).decode()
        if 'registro não compatível' in resp:
            print('\033[31mDesculpe mas a resposta do Servidor nos comunicou que seu endereço de Tel-mail e incompatível\033[m ')
            nome = input('Refaça se endereço de Tel-mail: ')
        else:
            trata_string(str(resp))
            desenha_email()
            print('\033[m')
    else:
        print('\033[31mDesculpe, mas o tipo de Tel-mail não foi encontrado \033[m')
input('Clique para sair')