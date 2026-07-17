from time import sleep
from editorIDE import desenhar
def pontos(quant):
    for c in range(quant):
        print('.', end=' ')
        sleep(0.5)
    print()
class Parser:
    def __init__ (self):
        self.memoria = []
    def iniciar(self):
        desenhar()
        print('       ParserTel')
        print('    iniciando',end=' ')
        pontos(3)
    def escolha(self):
        escolha = ''
        while escolha not in ['arquivo','pasta']:
            escolha = input('Os dados a serem lidos estão em formato de pasta ou arquivo:')
        if escolha == 'arquivo':
            arquivo_lido = input('qual o nome do arquivo a ser lido: ')
            achou = False
            for a in self.memoria:
                if a['nome'] == arquivo_lido and a['tipo'] == 'arq':
                    achou = True
                    print('   carregando arquivo',end=' ')
                    pontos(5)
                    if a['tipo arq'] == '.txt':
                        print(f'||nome do arquivo:{a['nome']}\n||registro de texto do arquivo:{a['dado']}')
                    else:
                        print(f'||nome do arquivo:{a['nome']}\n||registro numerico do arquivo:{a['dado']}')
                    print('processo finalizado com sucesso')
                    desenhar()
            if achou == False:
                print('arquivo não encontrado* provavelmente não existe')
                desenhar()
        elif escolha == 'pasta':
            pasta_lido = input('qual o nome da pasta a ser lida: ')
            achou = False
            for ai in self.memoria:
                if ai['nome'] == pasta_lido and ai['tipo'] == 'pasta':
                    achou = True
                    print('   carregando pasta',end=' ')
                    pontos(5)
                    for a in ai['dados']:
                        print(f'nome: {a['nome']}')
                    arquivo = input('qual o nome do arquivo a ser lido:')
                    achou = False
                    for a in ai['dados']:
                        if arquivo == a['nome']:
                            achou = True
                            ind = ai['dados'].index(a)
                            if a['tipo arq'] == '.txt':
                                print(f'||nome do arquivo:{a['nome']}\n||indice do arquivo:{ind}\n||registro de texto do arquivo:{a['dado']}')
                            else:
                                print(f'||nome do arquivo:{a['nome']}\n||indice do arquivo:{ind}\n||registro numerico do arquivo:{a['dado']}')
                            print('processo finalizado com sucesso')
                            desenhar()
                    if achou == False:
                        print('arquivo não encontrado* provavelmente não existe')
            if achou == False:
                print('pasta não encontrado* provavelmente não existe')
class AmbienteConfiguracoes:
    def __init__(self):
        self.config = {'cor area de trabalho': 'azul','tema da area de trabalho':'cinza'}
        self.nome_novo = ' '
        self.senha = ' '
    def iniciar(self):
        desenhar()
        print('         Configurações')
        print('     iniciando', end=' ')
        pontos(5)
        desenhar()
    def opcoes(self):
        desenhar()
        escolha = ''
        while escolha not in ['S', 'N']:
            escolha = input('Deseja mudar a cor da área de trabalho? (S/N): ').upper()

        if escolha == 'S':
            print('cor padrão: azul\n1) cor personalizada: roxo\n2) cor personalizada: verde\n3) cor personalizada: vermelho\n4) cor personalizada: amarelo')
            escolha2 = 0
            while escolha2 not in [ 1, 2 , 3 , 4]:
                try:
                    escolha2 = int(input('digite o índice da cor desejada: '))
                except ValueError:
                    print("Digite apenas 1 ou 2!")
            if escolha2 == 1:
                self.config['cor area de trabalho'] = 'roxo'
            elif escolha2 == 2:
                self.config['cor area de trabalho'] = 'verde'
            elif escolha2 == 3:
                self.config['cor area de trabalho'] = 'vermelho'
            elif escolha2 == 4:
                self.config['cor area de trabalho'] = 'amarelo'
            else:
                print('houve um erro tecnico raro ,por favor repetir escolha de cor')
            print(f"A cor escolhida foi: {self.config['cor area de trabalho']}")
        else:
            print("Mantendo a cor padrão: azul")
        desenhar()
        escolha2 = ' '
        while escolha2 not in ['S','N']:
            escolha2 = input('deseja mudar o nome do usuario:  ').upper()
        if escolha2 == 'S':
            print(f'o nome atual e este {self.nome_novo}')
            senha = input('digite a senha (para mudar): ')
            if senha == self.senha:
                nome_novo = input('digite o nome novo do usuario:')
                self.nome_novo = nome_novo
        else:
            print('nome de usuario mantido')
        desenhar()
        escolha = ' '
        while escolha not in ['S','N']:
            escolha = input('deseja mudar o tema da area de trabalho?: ').upper()
        if escolha == 'S':
            print('=========== temas disponiveis ==========\ntema padrão:calmo(cinza)\n1)tema personalizado:claro(branco)\n2)tema personalizado:escuro(preto)')
            escolha = 0
            while escolha not in [1,2]:
                escolha = int(input('Digite o indice do tema desejado:'))
            if escolha == 1:
                self.config['tema da area de trabalho'] = 'preto'
            else:
                self.config['tema da area de trabalho'] = 'branco'
        else:
            print('mantendo tema padrão:calmo(cinza)')
        desenhar()
amcom = AmbienteConfiguracoes()
parser1 = Parser()