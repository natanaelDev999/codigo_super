import socket
import time
usuario = []
#funções
def login_acesso():
    print(f'\033[36mpara acessar nosso serviço utilize seu login\033[m')
    pesquisa = input('que dados deseja acessar?: ')
    nome = input('Digite seu nome de usuario: ')
    escolha_senha = ''
    while escolha_senha not in ['S','N']:
        escolha_senha = input('Esqueceu sua senha?: ').upper().strip()
    if escolha_senha == 'N':
        senha = input('Digite sua senha para melhor validação: ')
        return str('2-1' + nome + ' '+pesquisa+  ' ' + senha)
    else:
        print('\033[34mok por favor espere\033[m')
        time.sleep(2)
        return str('2'+nome+' '+pesquisa+' '+'<senha>')
def login():
    global usuario
    nome = input('Crie um nome de usuario: ').strip()
    senha = int(input('Crie uma senha: '))
    usuario.append(nome)
    usuario.append(senha)
def mostropcoe():
    print('1)fazer o login\n2)acessar os serviços do servidor')
#configurações do servidor tcp cliente
port = 6001
ip = 'localhost'
socket_s2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_s2.connect((ip,port))
mostropcoe()
mensagem = ''
while mensagem not in ['1','2']:
    mensagem = input('Digite sua opção: ')
if mensagem == '1':
    login()
    string_list = '1' + usuario[0]+' '+str(usuario[1])
    socket_s2.send((string_list+'\n').encode())
if mensagem == '2':
    dados_valid = login_acesso()
    socket_s2.send((dados_valid+'\n').encode())
data = socket_s2.recv(1024).decode()
print('servidor respondeu: ',data)
socket_s2.close()