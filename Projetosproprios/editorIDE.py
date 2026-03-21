from time import sleep
def desenhar():
    print('=-' * 30)
def help():
    print('========== comandos poucos especiais =========\ndigite:(copy) para copiar arquivos (nome deve ser novo)\ndigite:(exit CommandTel) para sair do terminal\ndigite:(cp) para criar arquivos')
    print('digite:(vp) para visualizar arquivos')
def tempo():
    sleep(1)
    print('.', end=' ')
def jogo():
    mapa = [[2, 0, 1],
            [2, 0, 2],
            [2, 0, 0]]

    def mostrar_mapa():
        for linha in mapa:
            print(linha)

    mostrar_mapa()

    while True:
        escolha = input("Mover para onde (999 para parar)? (linha coluna): ")
        if escolha == '999':
            break
        if len(escolha) == 2:
            partes = escolha.split()
            nova_linha, nova_coluna = int(partes[0]), int(partes[1])

            linha_atual, coluna_atual = None, None
            for i in range(len(mapa)):
                for j in range(len(mapa[i])):
                    if mapa[i][j] == 1:
                        linha_atual, coluna_atual = i, j
                        break
                if linha_atual is not None:
                    break

            if mapa[nova_linha][nova_coluna] == 0:
                mapa[linha_atual][coluna_atual] = 0
                mapa[nova_linha][nova_coluna] = 1
            else:
                print('há uma parede nessa posição')

            mostrar_mapa()
        else:
            print('posição solicitada invalida')
class Editor:
    def __init__(self, tamanho_memoria):
        self.tamanho_memoria = tamanho_memoria
        self.memoria = []
    def iniciar_editor(self):
        desenhar()
        print(' ' * 10, 'abrindo TelEditor', end=' ')
        for r in range(5):
            tempo()
        print()
        desenhar()

    def rodar(self):
        escolha = ' '
        while escolha not in 'SN':
            escolha = input('Deseja modificar arquivo existente (S/N)? ').upper()
        if escolha == 'S':
             achou = False
             nome = input('qual o nome do arquivo que deseja modificar: ')
             for c in self.memoria:
                 if c['nome'] == nome:
                     achou = True
             if achou == True:
                 for c in self.memoria:
                     if c['nome'] == nome:
                        for n,l in c:
                           print(f'{n}: {l}')
                        pos = int(input('linha a mudar: '))
                        cod_novo = input('novo codigo >>>')
                        if 0 <= pos-1 < len(l):
                            l[pos-1][1] = cod_novo
                            print('mudaça feita')
                        else:
                            print('a linha solicitada não existe')
        else:
            cont = 1
            arquivo = []
            while True:
                linha = input(f'{cont}>>> ')
                if linha == 'fechar arquivo':
                    break
                arquivo.append([cont, linha])
                cont += 1
            nome_arq = input('Nome do arquivo: ')
            self.memoria.append({'nome':nome_arq,'tipo':'tel.','dado':arquivo})
            print(f"Arquivo '{nome_arq}' criado")

class Ide(Editor):
    def iniciar(self):
        desenhar()
        print(' ' * 15, 'iniciando TelIDE', end=' ')
        for r in range(5):
            tempo()
        print()
        desenhar()
        nome_arq2 = input('Arquivo para rodar: ')
        achou = False
        for a in self.memoria:
            if a['nome'] == nome_arq2:
                achou = True
        if achou == True:
            for a in self.memoria:
                if a['nome'] == nome_arq2:
                    variaveis = []
                    for l in a['dado']:
                        linha = l[1]
                        if linha.startswith('write >>'):
                            texto = linha[8:]
                            substituido = False
                            for v in variaveis:
                                if v['nome'] == texto:
                                    print(v['valor'])
                                    substituido = True
                                    break
                            if not substituido:
                                print(texto)
                        elif linha.startswith('let'):
                            partes = linha.split()
                            if len(partes) >= 4 and partes[2] == '=':
                                existe = any(v['nome'] == partes[1] for v in variaveis)
                                if not existe:
                                    variaveis.append({'nome': partes[1], 'valor': partes[3]})
                                else:
                                    print(f'erro: {partes[1]} já existe na memoria')
                                    break
        else:
            print('arquivo solicitado não foi encontrado *provavelmente não existe')
editor = Editor(360)
ide1 = Ide(360)
ide1.memoria = editor.memoria


