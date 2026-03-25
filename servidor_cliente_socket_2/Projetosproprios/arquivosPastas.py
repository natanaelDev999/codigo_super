import pandas as pd
pasta = list()
tipos = 0
tipoi = 0
nomes = []
for c in range(0,5):
    arquivos = list()
    nome = input('digite o nome do arquivo:')
    arquivos.append(nome)
    tipo = ' '
    while tipo not in 'IS':
        tipo = input('digite o tipo do arquivo: I para valor numerico S para valor com letras: ').upper().strip()
    arquivos.append(tipo)
    if tipo == 'I':
        valor = int(input('digite o valor para o arquivo:'))
        arquivos.append(valor)
        tipoi += 1
    if tipo == 'S':
        valor = str(input('digite o valor para o arquivo:'))
        arquivos.append(valor)
        tipos += 1
    pasta.append(arquivos)
    escolha = ' '
    while escolha not in 'SN':
        escolha = input('deseja continuar? [S/N]').strip().upper()[0]
    if escolha == 'N':
        break
for arquivos5 in pasta:
    nome = arquivos5[0]
    nomes.append(nome)
print('[1]ler arquivo\n[2]destruir arquivo\n[3]modificar arquivo\n[4]tabela de informações\n[5]sair do programa')
while True:
    escolha2 = ' '
    while escolha2 not in ['1','2','3','4','5']:
        escolha2 = input('digite sua escolha:')
    if escolha2 == '1':
        arquivode = input('digite o nome do arquivo:')
        for arquivo3 in pasta:
            if arquivo3[0] == arquivode:
                print(f'dado armazenado: {arquivo3[-1]}')
    if escolha2 == '2':
        arquivode = input('digite o nome do arquivo:')
        for arquivo3 in pasta:
            if arquivo3[0] == arquivode:
                if arquivo3[1] == 'S':
                    tipos -= 1
                elif arquivo3[1] == 'I':
                    tipoi -= 1
                nomes.remove(arquivo3[0])
                pasta.remove(arquivo3)
                print('arquivo removido com sucesso')
    if escolha2 == '3':
        arquivode = input('digite o nome do arquivo:')
        for arquivo3 in pasta:
            if arquivo3[0] == arquivode:
                if arquivo3[1] == 'S':
                    novodado = str(input('digite o dado para o arquivo:'))
                else:
                    novodado = int(input('digite o dado para o arquivo:'))
                arquivo3[2] = novodado
                print('arquivo modificado com sucesso')
    if escolha2 == '4':
        dados = {'tipo S': [f'{tipos}'], 'tipo I': [f'{tipoi}'], 'quant': [f'{len(pasta)}'],
                 'nomes arquivos': [f'{nomes}']}
        tabela = pd.DataFrame(dados)
        print(f'tabela de informações:\n{tabela}')
    if escolha2 == '5':
        print('saindo do programa')
        break
