import time as tm
from math import factorial
mathdowload = False
stringdowload = False
c_if = False
listaif = []
listanum = list()
lista = list()
listaw = list()
variaveis = list()
variaveisn = list()
pro = 0
end = 0
cont = 1
cod = ['program', 'write >>', 'end', 'rodar', 'let', 'loop', 'let input', 'let num', 'write >>>', 'let>num']
loop = 1
erros = 0
print('\033[34m=\033[m' * 40, '\033[34mIDE\033[m \033[33mTECTEL.1.0\033[m', '\033[34m=\033[m' * 36)
print('\033[34m=\033[m' * 30, 'ESCREVA SEU CODIGO EM \033[35mTETEL.1.0\033[m', '\033[34m=\033[m' * 30)
print('\033[34m=\033[m' * 93)

while True:
    or1 = input('')
    if or1.startswith('if'):
        partes = or1.split()
        if len(partes) == 4:
            var_nome, operador, valor = partes[1], partes[2], partes[3]
            for var in variaveis:
                if var[0] == var_nome:
                    if operador == '=' and var[1] == valor:
                        c_if = True
                        orw = input('   ')
                        listaif.append(orw)
                    else:
                        print('sinal de comparação \033[31minválido\033[m')
        else:
            print('\033[31merro\033[m: sintaxe do if incorreta')

    if or1 == 'write >>>':
        num1 = input('  ')
        num2 = input('  ')
        operacao = input('  ')
        achou1 = False
        achou2 = False
        for v in variaveisn:
            if v[0] == num1:
                num1 = v[1]
                achou1 = True
        for v in variaveisn:
            if v[0] == num2:
                num2 = v[1]
                achou2 = True
        if achou1 == False or achou2 == False:
            print('\033[31merro\033[m:variavel não encontrada na memoria')
            erros += 1
            continue
        else:
            if operacao == '+':
                soma = num1 + num2
                listanum.append(soma)
            elif operacao == '-':
                sub = num1 - num2
                listanum.append(sub)
            elif operacao == '*':
                mul = num1 * num2
                listanum.append(mul)
            elif operacao == '/':
                div = num1 / num2
                listanum.append(div)

    if or1 == 'loop':
        quant = int(input(' '))
        loop = quant

    comando_valido = (
        or1 in cod or
        or1.startswith("modulo") or
        or1.startswith("math>") or
        or1.startswith("string>") or
        or1.startswith("if")
    )

    if not comando_valido:
        print(f'\033[31merro\033[m função {or1} inválida')
        erros += 1
        continue

    elif or1.startswith('modulo'):
        partes = or1.split()
        if len(partes) > 1:
            if partes[1] == 'math':
                mathdowload = True
            if partes[1] == 'string':
                stringdowload = True

    if or1.startswith('string>') and stringdowload == True:
        partes = or1.split()
        if len(partes) > 1:
            if partes[1] == 'upper':
                string = str(input('    ')).upper()
                listaw.append(string)
            elif partes[1] == 'lower':
                string = str(input('    ')).lower()
                listaw.append(string)
            elif partes[1] == 'len<':
                string = str(input('    '))
                listanum.append(len(string))
            else:
                print(f'\033[31merro:\033[m função {or1} não encontrada no modulo')
                erros += 1
        else:
            print(f'\033[31merro:\033[m função {or1} não encontrada no modulo')
            erros += 1
    elif or1.startswith('string>') and stringdowload == False:
        print('\033[31merro\033[m: modulo não instalado')
        erros += 1

    if or1.startswith('math>') and mathdowload == True:
        partes = or1.split()
        if len(partes) > 1:
            if partes[1] == 'square_root':
                num = int(input('   '))
                raiz = num ** (1 / 2)
                listanum.append(raiz)
            elif partes[1] == 'cube_root':
                num = int(input('   '))
                raiz = num ** (1 / 3)
                listanum.append(raiz)
            elif partes[1] == 'factorial':
                num = int(input('   '))
                fatorial = factorial(num)
                listanum.append(fatorial)
            elif partes[1] == 'mediaTwo':
                soma = 0
                for c in range(0, 2):
                    num = int(input('   '))
                    soma += num
                media = soma / 2
                listanum.append(media)
            elif partes[1] == 'mediaBig':
                soma = 0
                cont_media = 0
                while True:
                    num = int(input('   '))
                    if num < 0:
                        break
                    cont_media += 1
                    soma += num
                if cont_media > 0:
                    media = soma / cont_media
                    listanum.append(media)
            else:
                print(f'\033[31merro\033[m: função {or1} não encontrada no modulo')
                erros += 1
        else:
            print(f'\033[31merro\033[m: função {or1} não encontrada no modulo')
            erros += 1
    elif or1.startswith('math>') and mathdowload == False:
        print('\033[31merro\033[m: modulo não instalado')
        erros += 1

    if cont == 1 and or1 != 'program':
        print('\033[31merro\033[m: o código deve começar com program')
        erros += 1
        continue

    if or1 == 'program':
        pro += 1
    elif or1 == 'end':
        end += 1
    elif or1 == 'let input':
        alvo = input("   ")
        variaveis.append([alvo, None])

    if or1 == 'let>num':
        var = input().split()
        if len(var) == 3 and var[1] == '=':
            achou = False
            for v in variaveisn:
                if v[0] == var[0]:
                    achou = True
            if achou == False:
                try:
                    valor = int(var[2])
                    variaveisn.append([var[0], valor])
                except ValueError:
                    print('\033[31merro\033[m: valor inválido para variavel numerica')
                    erros += 1
            else:
                print('\033[31merro\033[m:nome de variavel ja existe na memoria')
                erros += 1
        else:
            print('\033[31merro\033[m: sintaxe inválida, use ex: x = 5')
            erros += 1

    if or1 == 'let num':
        nome = input('n >  ')
        num1 = int(input('  '))
        num2 = int(input('  '))
        operacao = input('  ')
        achou = False
        for v in variaveisn:
            if v[0] == nome:
                achou = True
        if achou == False:
            if operacao == '+':
                soma = num1 + num2
                variaveisn.append([nome, soma])
            elif operacao == '-':
                menos = num1 - num2
                variaveisn.append([nome, menos])
            elif operacao == 'x':
                mul = num1 * num2
                variaveisn.append([nome, mul])
            elif operacao == '/':
                div = num1 / num2
                variaveisn.append([nome, div])
            elif operacao == '%':
                resto = num1 % num2
                variaveisn.append([nome, resto])
        else:
            print('\033[31merro\033[m:nome de variavel ja existe na memoria')
            erros += 1

    if or1 == 'let':
        entrada = input("   ")
        if "=" in entrada:
            nome, valor = entrada.split("=")
            nome = nome.strip()
            valor = valor.strip()
            achou = False
            for v in variaveis:
                if v[0] == nome:
                    achou = True
            if achou == False:
                variaveis.append([nome, valor])
            else:
                print('\033[31merro\033[m:nome de variavel ja existe na memoria')
                erros += 1

    elif or1 == 'write >>':
        orw = input("   ")
        listaw.append(orw)

    if or1 == 'rodar':
        if pro == end and pro > 0:
            print('/', '=' * 40, f'terminal / \033[33merros:\033[m {erros}')
            print('\033[35mEXECUTANDO O PROGRAMA\033[m', end=' ')

            def tempo():
                tm.sleep(0.7)

            tempo()
            print('.', end='')
            tempo()
            print('.', end='')
            tempo()
            print('.')

            for c in listaw:
                achou = False
                for var in variaveis:
                    if var[1] is None:
                        valor = input(f"    Digite um valor para {var[0]}: ")
                        var[1] = valor
                for var in variaveis:
                    if c == var[0]:
                        achou = True
                        if isinstance(var[1], str) and var[1].startswith("'") and var[1].endswith("'"):
                            for n in range(loop):
                                print(f'  {var[1][1:-1]}')
                        else:
                            for n in range(loop):
                                print(f'  {var[1]}')
                        break

                if not achou:
                    for var in variaveisn:
                        if c == var[0]:
                            achou = True
                            for n in range(loop):
                                print(f'  {var[1]}')
                            break

                if not achou:
                    if isinstance(c, str) and c.startswith("'") and c.endswith("'"):
                        for n in range(loop):
                            print(f'  {c[1:-1]}')
                    else:
                        print(f"erro: variável {c} não encontrada")
                        erros += 1

            if len(listanum) > 0:
                for v in range(loop):
                    for g in listanum:
                        print(f'  {g}')

            if c_if:
                for o in listaif:
                    print(f'  {o}')

            print('=' * 50)
            print('\033[35mprograma finalizado\033[m')
            break
        else:
            print('\033[31merro\033[m: número desigual de program e end')
            erros += 1

    cont += 1


'''c = False
listaif = []
listanum = list()
lista = list()
listaw = list()
variaveis = list()   # variáveis de texto e input
variaveisn = list()  # variáveis numéricas
pro = 0
end = 0
cont = 1
cod = ['program', 'write >>', 'end', 'rodar', 'let', 'loop', 'let input', 'let num','write >>>']
loop = 1
erros = 0
print('='*40,'IDLE TECTEL.1.0','='*36)
print('='*30,'ESCREVA SEU CODIGO EM TETEL.1.0','='*30)
print('='*93)
while True:
    or1 = input('')
    if or1.startswith('if'):
        or1.split()
        orw = input('   ')
        listaif.append(orw)
        for var in variaveis:
            if var[0] == or1[2]:
                item = var[1]
                if or1[2] == '=':
                    if item == var[3]:
                        c = True
                else:
                    print('sinal de comparação invalido')


    if or1 == 'write >>>':
        num1 = int(input('  '))
        num2 = int(input('  '))
        operacao = str(input('  '))
        if operacao == '+':
            soma = num1 + num2
            listanum.append(soma)
        if operacao == '-':
            sub = num1 - num2
            listanum.append(sub)
        if operacao == '*':
            mul = num1 * num2
            listanum.append(mul)
        if operacao == '/':
            div = num1 / num2
            listanum.append(div)
    # comando loop
    if or1 == 'loop':
        quant = int(input(' '))
        loop = quant

    # valida se comando existe ou se é comentário
    if not or1[0] == '&':
        if not or1[0:2] == 'if':
            if not or1 in cod:
                print(f'erro função {or1} invalida')
                erros += 1
                continue
        else:
            lista.append(or1)
    else:
        lista.append(or1)  # comentário é ignorado na execução

    # primeira instrução deve ser 'program'
    if cont == 1 and or1 != 'program':
        print('erro o codigo deve começar com program')
        erros += 1
        continue

    if or1 == 'program':
        pro += 1
    elif or1 == 'end':
        end += 1
    elif or1 == 'let input':
        alvo = input("   ")  # nome da variável
        variaveis.append([alvo, None])  # valor None por enquanto

    # variáveis numéricas
    if or1 == 'let num':
        nome = input('n >  ')
        num1 = int(input('  '))
        num2 = int(input('  '))
        operacao = input('  ')
        if operacao == '+':
            soma = num1 + num2
            variaveisn.append([nome, soma])
        if operacao == '-':
            menos = num1 - num2
            variaveisn.append([nome, menos])
        if operacao == 'x':
            mul = num1 * num2
            variaveisn.append([nome, mul])
        if operacao == '/':
            div = num1 / num2
            variaveisn.append([nome, div])
        if operacao == '%':
            resto = num1 % num2
            variaveisn.append([nome, resto])

    # variáveis de texto
    if or1 == 'let':
        entrada = input("   ")  # exemplo: x = 'Olá'
        if "=" in entrada:
            nome, valor = entrada.split("=")
            nome = nome.strip()
            valor = valor.strip()
            variaveis.append([nome, valor])

    # saída
    elif or1 == 'write >>':
        orw = input("   ")
        listaw.append(orw)

    # execução
    if or1 == 'rodar':
        if pro == end:
            print('/', '=' * 40, f'terminal / \033[33merros:\033[m {erros}')
            for c in listaw:
                achou = False

                # trata variáveis de texto/input
                for var in variaveis:
                    if var[1] is None:  # significa que foi 'let input'
                        valor = input(f"Digite um valor para {var[0]}: ")
                        var[1] = valor
                for var in variaveis:
                    if c == var[0]:
                        achou = True
                        if var[1].startswith("'") and var[1].endswith("'"):
                            for n in range(loop):
                                print(var[1][1:-1])
                        else:
                            for n in range(loop):
                                print(var[1])
                        break

                # trata variáveis numéricas
                if not achou:
                    for var in variaveisn:
                        if c == var[0]:
                            achou = True
                            for n in range(loop):
                                print(var[1])
                            break

                # caso seja string literal
                if not achou:
                    if c.startswith("'") and c.endswith("'"):
                        for n in range(loop):
                            print(c[1:-1])
                    else:
                        print(f"erro: variável {c} não encontrada")
                        erros += 1
            if len(listanum) > 0:
                for num in listanum:
                    print(num)
            if c:
                for o in listaif:
                    print(o)

            print('=' * 50)
            print('programa finalizado')
            break
        else:
            print('erro: número desigual de program e end')
            erros += 1

    cont += 1


# Armazenamento
lista = []
listaw = []
pro = 0
end = 0

# Funções para cada comando
def cmd_program():
    global pro
    pro += 1

def cmd_end():
    global end
    end += 1

def cmd_write():
    orw = input("   ")
    while orw[0] != "'" or orw[-1] != "'":
        print('erro', end='')
        orw = input("   ")
    listaw.append(orw)

def cmd_rodar():
    if pro == end:
        print('/', '='*40, 'terminal /')
        for c in listaw:
            print(c[1:-1])  # remove aspas
    else:
        print('erro')

def cmd_invalido():
    print("Comando inválido")

# Loop principal
while True:
    or1 = input('> ')
    lista.append(or1)

    if or1 == 'program':
        cmd_program()
    elif or1 == 'end':
        cmd_end()
    elif or1 == 'write >>':
        cmd_write()
    elif or1 == 'rodar':
        cmd_rodar()
    else:
        cmd_invalido()
class TetelInterpreter:
    def __init__(self):
        self.lista = []
        self.listaw = []
        self.pro = 0
        self.end = 0
        self.cont = 1

        # dicionário de comandos
        self.comandos = {
            "program": self.cmd_program,
            "end": self.cmd_end,
            "write >>": self.cmd_write,
            "rodar": self.cmd_rodar
        }

    def cmd_program(self):
        self.pro += 1

    def cmd_end(self):
        self.end += 1

    def cmd_write(self):
        orw = input("   ")
        while orw[0] != "'" or orw[-1] != "'":
            print('erro', end='')
            orw = input("   ")
        self.listaw.append(orw)

    def cmd_rodar(self):
        if self.pro == self.end:
            print('/', '='*40, 'terminal /')
            for c in self.listaw:
                print(c[1:-1])  # remove aspas
            self.listaw.clear()
            return True  # encerra execução
        else:
            print('erro')
        return False

    def cmd_invalido(self):
        print("Comando inválido")

    def run(self):
        while True:
            or1 = input('> ')
            self.lista.append(or1)

            # primeiro comando precisa ser 'program'
            if self.cont == 1 and or1 != "program":
                print("Primeiro comando precisa ser 'program'")
                continue

            func = self.comandos.get(or1, self.cmd_invalido)
            sair = func()
            if sair:
                break

            self.cont += 1


# Executando o interpretador Tetel 1.0
if __name__ == "__main__":
    TetelInterpreter().run()'''


