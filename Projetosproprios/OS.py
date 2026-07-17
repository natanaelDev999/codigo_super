from time import sleep
from configuracoes import amcom,parser1
import datetime
from editorIDE import editor, ide1, jogo, help
from random import randint
def desenhar():
    print('=-' * 30)

def tempo():
    sleep(1)
    print('.', end=' ')

def calculadora():
    desenhar()
    print('-=' * 15, 'Calculadora', '-=' * 20)
    desenhar()
    while True:
        operacao = input('digite a operação >>>')
        if not operacao == '999':
            partes = operacao.split()
            n1 = float(partes[0])
            n2 = float(partes[2])
            o = partes[1]
            if o == '+':
                print(n1 + n2)
            elif o == '-':
                print(n1 - n2)
            elif o == 'x':
                print(n1 * n2)
            elif o == '%':
                print(n1 / n2)
            else:
                print('operador invalido')
        else:
            desenhar()
            break
class Os:
    def __init__(self, tamanho_memoria):
        self.tamanho_memoria = tamanho_memoria
        self.confi = {'cor da area de trabalho':'azul','tema area de trabalho':'cinza'}
        self.memoria = []
        self.favoritos = []
        self.nome_usuario = ' '
        self.senha_usuario = ' '

    def iniciar(self):
        print(' '*10, 'TelOS', ' '*15)
        print('     iniciando', end=' ')
        for c in range(0, 5):
            tempo()
        print()
        desenhar()
        self.nome_usuario = str(input('digite o nome do usuario:'))
        self.senha_usuario = input('digite sua senha:')
        self.memoria.append({'nome': self.nome_usuario, 'tipo': 'user', 'senha': self.senha_usuario})
    def opcoes(self):
        desenhar()
        print('\033[34mdigite\033[m:(va) para visualizar os arquivos')
        print('\033[34mdigite\033[m:(ca) para criar arquivos')
        print('\033[34mdigite\033[m:(dea) para deletar arquivos')
        print('\033[34mdigite\033[m:(rea) para renomear arquivos')
        print('\033[34mdigite\033[m:(date) para saber a data')
        print('\033[34mdigite\033[m:(information) para saber de informações da maquina')
        print('\033[34mdigite\033[m:(help) para descobrir comandos pouco usados ')
    def terminal(self):
        desenhar()
        print('-='*15, 'TERMINALCommandTel', '-='*15)
        editor.memoria = self.memoria
        ide1.memoria = self.memoria
        while True:
            comando = input('> ')
            if comando == 'exit CommandTel':
                for c in range(0, 30):
                    print('/ ', end='')
                print()
                def tema():
                    if self.confi['tema area de trabalho'] == 'cinza':
                        print('=', '\033[37m' + ';' * 56 + '\033[m', '=')
                    elif self.confi['tema area de trabalho'] == 'branco':
                        print('=', '\033[30m' + ';' * 56 + '\033[m', '=')
                    elif self.confi['tema area de trabalho'] == 'preto':
                        print('=', '\033[m' + ';' * 56 + '\033[m', '=')
                while True:
                    for c in range(0, 10):
                        cor = self.confi.get('cor da area de trabalho', 'azul')
                        if cor == 'azul':
                            if c % 2 == 0:
                                print('=', '\033[36m' + ';' * 56 + '\033[m', '=')
                            else:
                                tema()
                        elif cor == 'roxo':
                            if c % 2 == 0:
                                print('=', '\033[35m' + ';' * 56 + '\033[m', '=')
                            else:
                                tema()
                        elif cor == 'verde':
                            if c % 2 == 0:
                                print('=', '\033[32m' + ';' * 56 + '\033[m', '=')
                            else:
                                tema()
                        elif cor == 'vermelho':
                            if c % 2 == 0:
                                print('=', '\033[31m' + ';' * 56 + '\033[m', '=')
                            else:
                                tema()
                        elif cor == 'amarelo':
                            if c % 2 == 0:
                                print('=', '\033[33m' + ';' * 56 + '\033[m', '=')
                            else:
                                tema()
                    desenhar()
                    procura = input('digite o aplicativo procurado:')
                    if procura == 'calculadora':
                        calculadora()
                    elif procura == 'exit TelOS':
                        return
                    elif procura == 'TelEditor':
                        editor.iniciar_editor()
                        editor.rodar()
                    elif procura == 'TelIDE':
                        ide1.iniciar()
                    elif procura == 'CommandTel':
                        return self.terminal()
                    elif procura == 'jogo':
                        jogo()
                    elif procura == 'configurações':
                        amcom.nome_novo = self.memoria[0]['nome']
                        amcom.senha = self.memoria[0]['senha']
                        amcom.iniciar()
                        amcom.opcoes()
                        self.confi['cor da area de trabalho'] = amcom.config['cor area de trabalho']
                        self.memoria[0]['nome'] = amcom.nome_novo
                        self.memoria[0]['senha'] = amcom.senha
                        self.confi['tema area de trabalho'] = amcom.config['tema da area de trabalho']
                    elif procura == 'ParserTel':
                        parser1.memoria = self.memoria
                        parser1.iniciar()
                        parser1.escolha()
                    else:
                        print('aplicativo não encontrado *provavelmente não existe ou não foi instalado')

            elif comando == 'va':
                desenhar()
                print('abrindo: explorador de arquivos', end=' ')
                for c in range(0, 5):
                    tempo()
                print()
                desenhar()
                if len(self.memoria) > 1:
                    for a in self.memoria:
                        if a['tipo'] == 'arq':
                            print(f"nome: {a['nome']} tipo: {a['tipo']} dado: {a['dado']} tamanho: {a['tamanho']} tipo de dado: {a['tipo arq']}")
                escolha = ' '
                while escolha not in 'SN':
                    escolha = input('deseja ver seus favoritos?:[S/N]').upper()
                if escolha == 'S':
                    if len(self.favoritos) > 0:
                        for a in self.favoritos:
                            print(f'nome: {a['nome']} tipo: {a['tipo']} dado: {a['dado']} tamanho: {a['tamanho']} tipo de dado: {a['tipo arq']}')
                    else:
                        print('não há nenhum arquivo na memoria')
                desenhar()

            elif comando == 'ca':
                desenhar()
                pro = False
                nome = ''
                while pro == False:
                    achou = False
                    while len(nome) == 0:
                        nome = input('digite o nome do arquivo:')
                        for a in self.memoria:
                            if a['nome'] == nome and a['tipo'] == 'arq':
                                achou = True
                    if not achou:
                        pro = True
                    else:
                        print('Já existe um arquivo com esse nome!')
                        nome = ''
                        desenhar()

                tipo_dado = ' '
                while tipo_dado not in ['C', 'N']:
                    tipo_dado = str(input('digite o tipo do dado: (C = caractere, N = numerica)')).upper()
                if tipo_dado == 'C':
                    dado = str(input('digite o dado do arquivo:'))
                    tamanho = len(dado)
                else:
                    dado = int(input('digite o dado do arquivo:'))
                    tamanho = len(str(dado))
                if tamanho <= self.tamanho_memoria:
                    self.tamanho_memoria -= tamanho
                    if tipo_dado == 'C':
                        self.memoria.append({'nome': nome, 'tipo': 'arq', 'dado': dado, 'tamanho': tamanho, 'tipo arq':'.txt'})
                    else:
                        self.memoria.append({'nome': nome, 'tipo': 'arq', 'dado': dado, 'tamanho': tamanho, 'tipo arq': '.num'})
                    print('arquivo criado')
                    escolha = ' '
                    while escolha not in 'SN':
                        escolha = input('deseja adicionar aos favoritos?:[S/N]').upper()
                    if escolha == 'S':
                        if tipo_dado == 'C':
                            self.favoritos.append({'nome': nome, 'tipo': 'arq', 'dado': dado, 'tamanho': tamanho, 'tipo arq':'.txt'})
                        else:
                            self.favoritos.append({'nome': nome, 'tipo': 'arq', 'dado': dado, 'tamanho': tamanho, 'tipo arq': '.num'})
                else:
                    print('não a espaço suficiente na memoria para esse arquivo')
                desenhar()

            elif comando == 'dea':
                desenhar()
                nome = input('digite o nome do arquivo:')
                achou = False
                for a in self.memoria:
                    if a['nome'] == nome:
                        achou = True
                if achou == True:
                    for a in list(self.memoria):
                        if a['nome'] == nome:
                            self.tamanho_memoria += a['tamanho']
                            self.memoria.remove(a)
                    print('arquivo removido')
                else:
                    print('o arquivo procurado não foi encontrado na memoria *provavelmente não existe')
                desenhar()
            elif comando == 'rea':
                desenhar()
                achou = False
                procurado = input('digite o nome do arquivo procurado:')
                for a in self.memoria:
                    if a['nome'] == procurado:
                        achou = True
                if achou == True:
                    print('arquivo encontrado')
                    nome_novo = input('escreva o nome novo: ')
                    for c in self.memoria:
                        if c['nome'] == procurado:
                            c['nome'] = nome_novo
                else:
                    print('arquivo não encontrado na memoria')
                desenhar()
            elif comando == 'date':
                desenhar()
                print(datetime.date.today())
                desenhar()
            elif comando == 'information':
                print('-'*48)
                print('data: ',datetime.date.today(),'=-'*15)
                print(f'usuario: {self.memoria[0]["nome"]}')
                print('memoria vazia:',self.tamanho_memoria,'; arquivos quantidade:',len(self.memoria)-1,)
                n = randint(0,236)
                situacao = ' '
                apli = ['calculadora','TelEditor','TelIDE','CommandTel','jogo','configurações']
                if n < 55:
                    situacao = 'eficacia critica'
                elif n < 120:
                    situacao = 'eficacia normal'
                elif n < 180:
                    situacao = 'intermediariamente eficaz'
                else:
                    situacao = 'altamente eficaz'
                print('uso da CPU:',n,f'situação da CPU: {situacao}')
                print('aplicativos disponiveis:')
                for c in apli:
                    print(f'                       -{c}')
                print('-' * 48)
            elif comando == 'deatot':
                desenhar()
                self.memoria = [self.memoria[0]]
                print('todos os arquivos foram removidos')
                desenhar()
            elif comando == 'help':
                desenhar()
                help()
                desenhar()
            elif comando == 'copy':
                desenhar()
                nome = input('digite o nome do arquivo a ser copiado: ')
                achou = False
                for a in self.memoria:
                    if a['nome'] == nome and a['tipo'] == 'arq':
                        achou = True
                if achou == True:
                    nome_novo = input('digite o novo nome do arquivo copiado:')
                    if nome == nome_novo:
                        print('o nome novo deve ser diferente do copiado')
                    else:
                        arq = {'nome':nome_novo,'tipo':a['tipo'],'dado': a['dado'],'tamanho':a['tamanho'],'tipo arq':a['tipo arq']}
                        self.memoria.append(arq)
                        print('arquivo copiado')
                        escolha = ' '
                        while escolha not in ['S','N']:
                            escolha = input('deseja adicionar aos favoritos?: ')
                        if escolha == 'S':
                            self.favoritos.append(arq)
                else:
                    print('arquivo solicitado não encontrado *provavelmente não existe')

                    desenhar()
            elif comando == 'cp':
                desenhar()
                nome = input('qual o nome da pasta:')
                achou = False
                for a in self.memoria:
                    if a['nome'] == nome and a['tipo'] == 'pasta':
                        achou = True
                if achou == True:
                    print('ja a uma pasta com o mesmo nome')
                else:
                    pasta = {'nome':nome,'tipo':'pasta'}
                    arquivos = []
                    tamanhot = 0
                    print('     abrindo a pasta      \n   iniciando',end=' ')
                    for c in range(0,5):
                        tempo()
                    print()
                    desenhar()
                    quant = int(input('quantos arquivos tera (muitos ira ocupar muito a memoria)?: '))
                    certeza = input(f'deseja mesmo {quant} arquivos:[S/N]').upper()[0]
                    if certeza == 'S':
                        for c in range(0,quant):
                            desenhar()
                            pro = False
                            nome = ''
                            while pro == False:
                                achou = False
                                while len(nome) == 0:
                                    nome = input('digite o nome do arquivo:')
                                    for a in self.memoria:
                                        if a['nome'] == nome and a['tipo'] == 'arq':
                                            achou = True
                                if not achou:
                                    pro = True
                                else:
                                    print('Já existe um arquivo com esse nome!')
                                    nome = ''
                                    desenhar()

                            tipo_dado = ' '
                            while tipo_dado not in ['C', 'N']:
                                tipo_dado = str(input('digite o tipo do dado: (C = caractere, N = numerica)')).upper()
                            if tipo_dado == 'C':
                                dado = str(input('digite o dado do arquivo:'))
                                tamanho = len(dado)
                            else:
                                dado = int(input('digite o dado do arquivo:'))
                                tamanho = len(str(dado))
                            if tamanho <= self.tamanho_memoria:
                                self.tamanho_memoria -= tamanho
                                if tipo_dado == 'C':
                                    arquivos.append(
                                        {'nome': nome, 'tipo': 'arq', 'dado': dado, 'tamanho': tamanho, 'tipo arq': '.txt'})
                                else:
                                    arquivos.append(
                                        {'nome': nome, 'tipo': 'arq', 'dado': dado, 'tamanho': tamanho, 'tipo arq': '.num'})
                                print('arquivo criado e adicionado a pasta')
                            else:
                                print('não a espaço suficiente na memoria para esse arquivo')
                            tamanhot += tamanho
                            desenhar()
                        pasta['dados'] = arquivos
                        pasta['tamanho'] = tamanhot
                        self.memoria.append(pasta)
                    else:
                        print('por favor refazer o processo')
                    desenhar()
            elif comando == 'vp':
                desenhar()
                achou = False
                for a in self.memoria:
                    if a['tipo'] == 'pasta':
                        achou = True
                if achou == True:
                    for a in self.memoria:
                        if a['tipo'] == 'pasta':
                            print(f'nome da pasta :{a['nome']}\ntamanho da pasta: {a['tamanho']}')
                            for a in a['dados']:
                                print(f"nome: {a['nome']} tipo: {a['tipo']} dado: {a['dado']} tamanho: {a['tamanho']} tipo de dado: {a['tipo arq']}")
                else:
                    print('não a nenhuma pasta na memoria')
                desenhar()
            else:
                print('comando invalido')

os1 = Os(360)
os1.iniciar()
os1.opcoes()
os1.terminal()


