import datetime
def login():
    usuario = input('Crie um nome de usuario: ')
    senha = input('Crie uma senha para seu usario: ')
    arquivo = open('usuarios_request.txt','r+')
    achou = False
    tamanho = arquivo.read()
    if len(tamanho) > 0:
        arquivo.seek(0)
        for usuario2 in arquivo:
            usuario2 = usuario2.strip()
            nome, sen = usuario2.split(';')
            if usuario == nome:
                achou = True
            if achou == True:
                print('informações de cadastro ja existem')
                break
    if len(tamanho) == 0:
        arquivo.write(f'{usuario};{senha}')
        print('adicionado com sucesso')
    elif achou == False and usuario not in tamanho:
        arquivo.write(f'\n{usuario};{senha}')
        print('adicionado com sucesso')
    arquivo.close()
achou = False
usuario = []
def request_acesso():
    global achou
    global usuario
    achou = False
    usuario = []
    arquivo = open('usuarios_request.txt','r+')
    nome_acesso = input('Digite seu nome de usuario para utilizar o serviço de request\n:')
    usuarios = arquivo.read()
    if len(usuarios) > 0:
        arquivo.seek(0)
        for usuario_acesso in arquivo:
            nome, sen = usuario_acesso.strip().split(';')
            if nome_acesso == nome:
                achou = True
                usuario.append(nome)
        if achou == False:
            print('usuario não existe')
    else:
        print('não há usuarios cadastrados')
    arquivo.close()
def request():
    global achou
    global usuario
    arquivo = open('servidor_de_mentira_request.txt','a+')
    if achou == True:
        arquivo.write(f'\nregistro de acesso:usuario:{usuario[0]};data de acesso:{datetime.date.today()}')
        request_desejo = input('qual dado você deseja acessar: ')
        arquivo.seek(0)
        for dado in arquivo:
            if request_desejo in dado.strip() or request_desejo == dado.strip():
                print(f'dado achado: {dado.strip()}')
    else:
        print('acesso negado')
    arquivo.close()
def escolha():
    print('Serviço de request do servidor DataNatan\n*Servidor:É sistema hardware ou software que fornece serviços,dados ... para um chamado ''cliente'' ')
    print('O serviço de request e um serviço que fornece aos usuarios dados publicos ,para acessa-los escolha 1 se não escolha 2 ')
    print('1)fazer registro para acesso ao request\n2)acessar serviço de request')
    escolha = ' '
    while escolha not in ['1','2']:
        escolha = input('deseja utilizar qual serviço: ')
    if escolha == '1':
        login()
    else:
        request_acesso()
        request()
escolha()
