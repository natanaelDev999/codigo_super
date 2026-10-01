import math

#                           TelShader
#A linguagem de sombreamento do terminal

def compila_codigo_telshader(codigo_TelShader,pixel,x,y,bdm={}):
    pixel_saida = ' '
    linha = ''
    variaveis = []
    vetor = []
    ativ_case = False
    for c in codigo_TelShader:
        if c != ';':
            linha += c
        else:
            linha = linha.strip()
            if linha.startswith('$') or not linha.startswith('$'):
                if ativ_case == True or not linha.startswith('$'):
                    if linha.startswith('$'):
                        linha = linha[1:]
                    # dá a uma variável o valor de um vetor
                    if linha.startswith('dva'):
                        comando , vetor1 , pos , var = linha.split(' ')
                        for v in vetor:
                            if v[0] == vetor1:
                                for i in variaveis:
                                    if i[0] == var:
                                        i[1] = v[1][f"{pos}"]
                    # multiplica um vetor por uma matriz
                    elif linha.startswith('mvm'):
                        comando , pos_m , vetor1 = linha.split(' ')
                        if vetor1 != "vecXY":
                            for v in vetor:
                                if v[0] == vetor1:
                                    for pos0,n in enumerate(bdm[f"{pos_m}"]):
                                        soma = 0
                                        for pos1, n1 in enumerate(n):
                                            soma += n1 * v[1][f"{pos1}"]
                                        v[1][f"{pos0}"] = soma
                                    break
                        else:
                            for pos0, n in enumerate(bdm[f"{pos_m}"]):
                                soma = 0
                                for pos1, n1 in enumerate(n):
                                    if pos1 == 0:
                                        soma += n1 * x
                                    elif pos1 == 1:
                                        soma += n1 * y
                                if pos0 == 0:
                                    x = soma
                                elif pos0 == 1:
                                    y = soma
                    # termina condicional
                    elif linha.startswith('ec'):
                        ativ_case = False
                    # trata condicionais
                    elif linha.startswith('case'):
                        comando, valor1 , comp , valor2 = linha.split(' ')
                        if valor1 == 'x':
                            valor1 = float(x)
                        elif valor1 == 'y':
                            valor1 = float(y)

                        if valor2 == 'x':
                            valor2 = float(x)
                        elif valor2 == 'y':
                            valor2 = float(y)

                        if type(valor1) == str:
                            if valor1.isnumeric():
                                valor1 = float(valor1)
                            else:
                                for i in variaveis:
                                    if i[0] == valor1:
                                        valor1 = float(i[1])

                        if type(valor2) == str:
                            if valor2.isnumeric():
                                valor2 = float(valor2)
                            else:
                                for i in variaveis:
                                    if i[0] == valor1:
                                        valor2 = float(i[1])

                        if type(valor1) == float and type(valor2) == float:
                            if comp == '==':
                                if valor1 == valor2:
                                    ativ_case = True

                            elif  comp  == '>':
                                if valor1 > valor2:
                                    ativ_case = True

                            elif  comp  == '<':
                                if valor1 < valor2:
                                    ativ_case = True

                            elif  comp  == '!':
                                if valor1 != valor2:
                                    ativ_case = True

                            elif comp == '%':
                                if valor1 % valor2 == 0:
                                    ativ_case = True

                            elif comp == '%?':
                                if valor1 % valor2 != 0:
                                    ativ_case = True
                    # modifica o caractere do pixel
                    if linha.startswith('p=') or linha.startswith('p ='):
                        vars,chr = linha.split('=')
                        if chr == 'pr':
                            pixel_saida = pixel
                        else:
                            pixel_saida = chr
                    # modifica a cor do pixel
                    elif linha.startswith('cp=') or linha.startswith('cp ='):
                        vars,chr = linha.split('=')
                        if ',' in chr:
                            r,g,b = chr.split(',')
                            pixel_saida = f'\033[38;2;{r};{g};{b}m{pixel_saida}\033[m'
                        else:
                            for v in vetor:
                                if v[0] == chr:
                                    if v[2] == 'vec3':
                                        r = v[1]["0"]
                                        g = v[1]["1"]
                                        b = v[1]["2"]
                                        pixel_saida = f'\033[38;2;{int(r)};{int(g)};{int(b)}m{pixel_saida}\033[m'
                    # dá valor ao x
                    elif linha.startswith('x=') or linha.startswith('x ='):
                        vars,pos = linha.split('=')
                        if pos.isnumeric():
                            x = int(pos)
                        else:
                            for i in variaveis:
                                if i[0] == pos:
                                    x = i[1]
                                    break
                    # dá valor ao y
                    elif linha.startswith('y=') or linha.startswith('y ='):
                        vars,pos = linha.split('=')
                        if pos.isnumeric():
                            y = int(pos)
                        else:
                            for i in variaveis:
                                if i[0] == pos:
                                    y = i[1]
                    # soma um certo valor de algum elemento do vecXY
                    elif linha.startswith('v'):
                        operacao, valor1, valor2 = linha.split(' ')
                        if valor1 == 'x':
                            if valor2.isnumeric():
                                x += float(valor2)
                            else:
                                for i in variaveis:
                                    if i[0] == valor2:
                                        x += i[1]
                                        break
                        elif valor1 == 'y':
                            if valor2.isnumeric():
                                y += float(valor2)
                            else:
                                for i in variaveis:
                                    if i[0] == valor2:
                                        y += i[1]
                                        break
                    # subrai um certo valor de algum elemento do vecXY
                    elif linha.startswith('s'):
                        operacao, valor1, valor2 = linha.split(' ')
                        if valor1 == 'x':
                            if valor2.isnumeric():
                                x -= int(valor2)
                            else:
                                for i in variaveis:
                                    if i[0] == valor2:
                                        x -= i[1]
                                        break
                        elif valor1 == 'y':
                            if valor2.isnumeric():
                                y -= int(valor2)
                            else:
                                for i in variaveis:
                                    if i[0] == valor2:
                                        y -= i[1]
                                        break
                    # cria uma variavel do tipo float
                    elif linha.startswith('ptf'):
                        comando, nome , valor = linha.split(' ')
                        if valor.isnumeric():
                            variaveis.append([nome,float(valor)])
                        else:
                            for i in variaveis:
                                if i[0] == valor:
                                    variaveis.append([nome,i[1]])
                                    break
                    # criar um vec2 que suport float
                    elif linha.startswith('2ptf'):
                        comando, nome = linha.split(' ')
                        if nome != 'vecXY':
                            vetor.append([nome,{"0":0,"1":0},"vec2"])
                    # cria um vec3 que suporta float
                    elif linha.startswith('3ptf'):
                        comando, nome = linha.split(' ')
                        if nome != 'vecXY':
                            vetor.append([nome,{"0":0,"1":0,"2":0},"vec3"])
                    # modifica um vetor
                    elif linha.startswith('mdf'):
                        comando, nome , pos , valor = linha.split(' ')
                        if valor.isnumeric():
                            for v in vetor:
                                if v[0] == nome:
                                    v[1][f"{pos}"] = float(valor)
                                    break
                        else:
                            for v in vetor:
                                if v[0] == nome:
                                    for l in variaveis:
                                        if l[0] == valor:
                                            v[1][f"{pos}"] = float(l[1])
                                            break
                                    break
                    # soma vetores
                    elif linha.startswith('unv'):
                        comando, vetor1, vetor2 = linha.split(' ')
                        for v in vetor:
                            if v[0] == vetor1:
                                for v2 in vetor:
                                    if v2[0] == vetor2:
                                        if v[2] == "vec3":
                                            v[1]["0"] = v[1]["0"] + v2[1]["0"]
                                            v[1]["1"] = v[1]["1"] + v2[1]["1"]
                                            v[1]["2"] = v[1]["2"] + v2[1]["2"]
                                        elif v[2] == 'vec2':
                                            v[1]["0"] = v[1]["0"] + v2[1]["0"]
                                            v[1]["1"] = v[1]["1"] + v2[1]["1"]
                    # subtrai vetores
                    elif linha.startswith('uns'):
                        comando, vetor1, vetor2 = linha.split(' ')
                        for v in vetor:
                            if v[0] == vetor1:
                                for v2 in vetor:
                                    if v2[0] == vetor2:
                                        if v[2] == "vec3":
                                            v[1]["0"] = v[1]["0"] - v2[1]["0"]
                                            v[1]["1"] = v[1]["1"] - v2[1]["1"]
                                            v[1]["2"] = v[1]["2"] - v2[1]["2"]
                                        elif v[2] == 'vec2':
                                            v[1]["0"] = v[1]["0"] - v2[1]["0"]
                                            v[1]["1"] = v[1]["1"] - v2[1]["1"]
                    # multiplica vetores
                    elif linha.startswith('muv'):
                        comando, vetor1, vetor2 = linha.split(' ')
                        for v in vetor:
                            if v[0] == vetor1:
                                for v2 in vetor:
                                    if v2[0] == vetor2:
                                        if v[2] == "vec3":
                                            v[1]["0"] = v[1]["0"] * v2[1]["0"]
                                            v[1]["1"] = v[1]["1"] * v2[1]["1"]
                                            v[1]["2"] = v[1]["2"] * v2[1]["2"]
                                        elif v[2] == 'vec2':
                                            v[1]["0"] = v[1]["0"] * v2[1]["0"]
                                            v[1]["1"] = v[1]["1"] * v2[1]["1"]
                    # divide vetores
                    elif linha.startswith('fiv'):
                        comando, vetor1, vetor2 = linha.split(' ')
                        for v in vetor:
                            if v[0] == vetor1:
                                for v2 in vetor:
                                    if v2[0] == vetor2:
                                        if v[2] == "vec3":
                                            if v2[1]["0"] != 0:
                                                v[1]["0"] = v[1]["0"] / v2[1]["0"]
                                            else:
                                                v[1]["0"] = v[1]["0"] / 1

                                            if v2[1]["1"] != 0:
                                                v[1]["1"] = v[1]["1"] / v2[1]["1"]
                                            else:
                                                v[1]["1"] = v[1]["1"] / 1

                                            if v2[1]["2"] != 0:
                                                v[1]["2"] = v[1]["2"] / v2[1]["2"]
                                            else:
                                                v[1]["2"] = v[1]["2"] / 1
                                        elif v[2] == 'vec2':
                                            if v2[1]["0"] != 0:
                                                v[1]["0"] = v[1]["0"] / v2[1]["0"]
                                            else:
                                                v[1]["0"] = v[1]["0"] / 1

                                            if v2[1]["1"] != 0:
                                                v[1]["1"] = v[1]["1"] / v2[1]["1"]
                                            else:
                                                v[1]["1"] = v[1]["1"] / 1
                    # copia vetor
                    elif linha.startswith('pyc'):
                        comando, vetor1, vetor2 = linha.split(' ')
                        if vetor1 != 'vecXY':
                            for v in vetor:
                                if v[0] == vetor1:
                                    for v2 in vetor:
                                        if v2[0] == vetor2:
                                            if v[2] == "vec3":
                                                v[1]["0"] = v2[1]["0"]
                                                v[1]["1"] = v2[1]["1"]
                                                v[1]["2"] = v2[1]["2"]
                                            elif v[2] == "vec2":
                                                v[1]["0"] = v2[1]["0"]
                                                v[1]["1"] = v2[1]["1"]
                        else:
                            for v in vetor:
                                if v[0] == vetor2:
                                    x = v[1]["0"]
                                    y = v[1]["1"]
                    # atribui a uma variavel o produto escalar de um vetor
                    elif linha.startswith('dot'):
                        comando, var, vetor1, vetor2 = linha.split(' ')
                        for i in variaveis:
                            if i[0] == var:
                                for v in vetor:
                                    if v[0] == vetor1:
                                        for v2 in vetor:
                                            if v2[0] == vetor2:
                                                dot = 0
                                                if v[2] == 'vec3':
                                                    dot += float(v[1]["0"])*float(v2[1]["0"])
                                                    dot += float(v[1]["1"])*float(v2[1]["1"])
                                                    dot += float(v[1]["2"])*float(v2[1]["2"])
                                                elif v[2] == 'vec2':
                                                    dot += float(v[1]["0"]) * float(v2[1]["0"])
                                                    dot += float(v[1]["1"]) * float(v2[1]["1"])
                                                i[1] = dot
                                                break
                    # normaliza um vetor
                    elif linha.startswith('nrm'):
                        comando, vetor1 = linha.split(' ')
                        divisor = 0
                        for v in vetor:
                            if v[0] == vetor1:
                                if v[2] == 'vec3':
                                    divisor += v[1]["0"]**2
                                    divisor += v[1]["1"] ** 2
                                    divisor += v[1]["2"] ** 2

                                    divisor = math.sqrt(divisor)

                                    v[1]["0"] = v[1]["0"]/divisor
                                    v[1]["1"] = v[1]["1"] / divisor
                                    v[1]["2"] = v[1]["2"] / divisor
            linha = ''
    return [pixel_saida,int(x),int(y)]