
'''for c in range(0,4):
    nome = input('Digite seu nome de usuario: ')
    senha = input('Digite sua senha:')
    arquivo = open('dados.txt','r+')
    lin1 = arquivo.read()
    if len(lin1) == 0:
        arquivo.write(nome+'\n')
        arquivo.write(senha)
    else:
        arquivo.write(f'\n{nome}\n')
        arquivo.write(senha)
    arquivo.close()'''
arquivo = open('dados.txt', 'rb')
print(arquivo.read())
arquivo.close()