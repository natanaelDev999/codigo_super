import socket

obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

obj.connect(('localhost',7900))
nome = ''
while not '@' in nome:
    nome = input('Crie um endereço de \033[34mTel-mail\033[m: ')
    if not '@' in nome:
        print('\033[31mDesculpa mas o endereço tem que ter um @\033[m')
while True:
    para = input('Para: ')
    print('\033[34m-'*20,'\033[m')
    email = input('Email(exit- para sair): ')
    if 'exit-' in email:
        obj.send('exit-'.encode())
        break
    obj.send((para+'/'+email+'/'+nome).encode())
    resp = obj.recv(1024).decode()
    if 'registro não compatível' in resp:
        print('\033[31mDesculpe mas a resposta do Servidor nos comunicou que seu endereço de Tel-mail e incompatível\033[m ')
        nome = input('Refaça se endereço de Tel-mail: ')
    else:
        print('[SERVIDOR] respondeu: ',resp)