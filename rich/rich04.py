from rich import print
from rich import inspect
import os
inspect(str)
class Os:
    '''
    inicia o TelOS que proporciona otimo processamento e varios softwares
    '''
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
        self.nome_usuario = str(input('digite o nome do usuario:'))
        self.senha_usuario = input('digite sua senha:')
        self.memoria.append({'nome': self.nome_usuario, 'tipo': 'user', 'senha': self.senha_usuario})
    def opcoes(self):
        print('\033[34mdigite\033[m:(va) para visualizar os arquivos')
        print('\033[34mdigite\033[m:(ca) para criar arquivos')
        print('\033[34mdigite\033[m:(dea) para deletar arquivos')
        print('\033[34mdigite\033[m:(rea) para renomear arquivos')
        print('\033[34mdigite\033[m:(date) para saber a data')
        print('\033[34mdigite\033[m:(information) para saber de informações da maquina')
        print('\033[34mdigite\033[m:(help) para descobrir comandos pouco usados ')
os1 = Os(360)
inspect(os1)