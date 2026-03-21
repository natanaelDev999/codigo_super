escreva = ['write>>']
let = ['let']
ini = ['program']
fim = ['end']
loop = ['loop']
escrevatipo = ['writeType']
escrevavet = ['writeVet']
vetores = ['vet']
writenum = ['writnum']
variaveiscom = []
variaveis = []
saida = []
loops = []

programas = []
bloco_atual = []
nome_programa = ""

erro = 0

while True:
    or1 = input('')
    if or1.startswith(writenum[0]):
        partes = or1.split()
        num1 = partes[1]
        num2 = partes[3]
        operador = partes[2]
        achou1 = False
        achou2 = False
        for v in variaveis:
            if v[0] == num1:
                if v[2] == 'int':
                    achou1 = True
                    num1 = v[1]
                else:
                    erro += 1
        for v in variaveis:
            if v[0] == num2:
                if v[2] == 'int':
                    achou2 = True
                    num2 = v[1]
        if achou1 == False and achou2 == False:
            erro += 1
        else:
            if operador == '+':
                soma = num1 + num2
                saida.append(soma)
            elif operador == '-':
                sub = num1 - num2
                saida.append(sub)
            elif operador == '*':
                mul = num1 * num2
                saida.append(mul)
            elif operador == '/':
                div = num1 / num2
                saida.append(div)

    if or1.startswith("program"):
        partes = or1.split()
        nome_programa = partes[1]
        bloco_atual = []
        continue

    if or1.startswith("end"):
        partes = or1.split()
        if partes[1] != nome_programa:
            erro += 1
        else:
            programas.append(bloco_atual.copy())
        continue

    if or1 != "rodar":
        bloco_atual.append(or1)

    if or1.startswith(vetores[0]):
        partes = or1.split()
        variaveiscom.append([partes[1], partes[2:], partes[0]])

    if or1.startswith(escrevavet[0]):
        num = int(input('   '))
        partes = or1.split()
        achou = False
        for var in variaveiscom:
            if var[0] == partes[1] and num < len(var[1]):
                saida.append(var[1][num])
                achou = True
        if not achou:
            erro += 1

    if or1.startswith(escrevatipo[0]):
        partes = or1.split()
        alvo = partes[1]
        encontrado = False

        for v in variaveis:
            if v[0] == alvo:
                saida.append(v[2])
                encontrado = True

        for v in variaveiscom:
            if v[0] == alvo:
                saida.append(v[2])
                encontrado = True

        if not encontrado:
            erro += 1

    if or1.startswith(loop[0]):
        loopnum = int(input('   '))
        comandos_loop = []
        while True:
            cod = input('   ')
            if cod == 'endloop':
                loops.append([comandos_loop, loopnum])
                break
            comandos_loop.append(cod)
        continue

    if or1.startswith(let[0]):
        partes = or1.split()
        tipo = partes[1]
        nome_var = partes[2]
        valor = partes[4]
        if tipo == 'int':
            variaveis.append([nome_var, int(valor), tipo])
        else:
            variaveis.append([nome_var, valor, tipo])

    if or1.startswith(escreva[0]):
        partes = or1.split()
        alvo = partes[1]
        achou = False
        for v in variaveis:
            if v[0] == alvo:
                saida.append(v[1])
                achou = True
                break
        if not achou:
            saida.append(or1[7:])

    if or1 == "rodar":
        print('/', '=' * 40, f'terminal /')

        if erro == 0:
            for s in saida:
                print(s)

            for bloco, vezes in loops:
                for _ in range(vezes):
                    for cmd in bloco:
                        if cmd.startswith(escreva[0]):
                            partes = cmd.split()
                            alvo = partes[1]
                            achou = False
                            for v in variaveis:
                                if v[0] == alvo:
                                    print(v[1])
                                    achou = True
                                    break
                            if not achou:
                                print(cmd[7:])
            break

        else:
            print("erro de sintaxe no código")
            break

'''escreva = ['write>>']
let = ['let']
ini = ['program']
fim = ['end']
loop = ['loop']
escrevatipo = ['writeType']
variaveis = []
saida = []
loops = []
cp = ce = erro = 0
cont = 1
nome = ''
cont2 = 0
quantint = 0
quantstr = 0
g = False
while True:
    achou = False
    or1 = input('')
    if or1.startswith(escrevatipo[0]):
        partes = or1.split()
        for v in variaveis:
            if v[0] == partes[1]:
                if v[2] == 'str' or v[2] == 'int':
                    saida.append(v[2])
                    g = True
                else:
                    erro += 1
        if g == False:
            erro += 1
    if or1.startswith(loop[0]):
        loopnum = int(input('   '))
        comandos_loop = []
        while True:
            cod = input('   ')
            if cod == 'endloop':
                loops.append([comandos_loop, loopnum])
                break
            comandos_loop.append(cod)
        continue
    if cont == 1:
        partes = or1.split()
        if partes[0] == ini[0]:
            nome = partes[1]
            cp += 1
        else:
            erro += 1
    if or1.startswith(let[0]):
        partes = or1.split()
        if partes[1] == 'str' or partes[1] == 'int':
            variaveis.append([partes[2], partes[4],partes[1]])
        else:
            erro += 1
    if or1.startswith(escreva[0]):
        partes = or1.split()
        achou = False
        for v in variaveis:
            if v[0] == partes[1]:
                saida.append(v[1])
                achou = True
                break
        if not achou:
            saida.append(or1[7:])
    if or1.startswith(fim[0]):
        partes = or1.split()
        if partes[1] != nome:
            erro += 1
        else:
            ce += 1
    if or1 == 'rodar':
        print('/', '=' * 40, f'terminal /')
        if erro == 0 and ce == 1 and cp == 1:
            for s in saida:
                print(s)
            for bloco, vezes in loops:
                for _ in range(vezes):
                    for cmd in bloco:
                        if cmd.startswith(escreva[0]):
                            partes = cmd.split()
                            achou = False
                            for v in variaveis:
                                if v[0] == partes[1]:
                                    print(v[1])
                                    achou = True
                                    break
                            if not achou:
                                print(cmd[7:])
            print('='*30,'ANALISE DO CODIGO','='*30)
            print(f'foram declaradas no total {len(variaveis)} variaveis ')
            for v in variaveis:
                if v[2] == 'int':
                    quantint += 1
                else:
                    quantstr += 1
            print(f'foram declaradas {quantint} variaveis numericas')
            print(f'foram declaradas {quantstr} variaveis alfabeticas')
            for v in variaveis:
                print(f'nome: {v[0]} valor: {v[1]} tipo: {v[2]}')
            break
        else:
            print("erro de sintaxe no código")
            break
    cont += 1'''
