
#                           TelMatrixShader
#A linguagem de vértice do terminal
def compila_codigo_telmatrixshader(codigo_TelMatrixShader, vertice,bdm):
    vertice_saida = []
    # vetores
    vetores = [['vecI',{'x':vertice[0],'y':vertice[1],'z':vertice[2]}],['vecO',{'x':0,'y':0,'z':0}]]
    # variáveis
    variaveis = []
    # lê código
    linha = ''
    # codição
    ativ_case = False
    for c in codigo_TelMatrixShader:
        if c != ';':
            linha += c
        else:
            linha = linha.strip()
            if linha.startswith('$') or not linha.startswith('$'):
                if ativ_case == True or not linha.startswith('$'):
                    if linha.startswith('$'):
                        linha = linha[1:]
                    # trata condicionais
                    if linha.startswith('ec'):
                        ativ_case = False
                    if linha.startswith('case'):
                        comando, valor1, comp, valor2 = linha.split(' ')

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

                            elif comp == '>':
                                if valor1 > valor2:
                                    ativ_case = True

                            elif comp == '<':
                                if valor1 < valor2:
                                    ativ_case = True

                            elif comp == '!':
                                if valor1 != valor2:
                                    ativ_case = True

                            elif comp == '>=':
                                if valor1 >= valor2:
                                    ativ_case = True

                            elif comp == '<=':
                                if valor1 <= valor2:
                                    ativ_case = True

                            elif comp == '%':
                                if valor1 % valor2 == 0:
                                    ativ_case = True

                            elif comp == '%?':
                                if valor1 % valor2 != 0:
                                    ativ_case = True
                    # modifica o valor de uma variável
                    if linha.startswith('mdv'):
                        comando, variavel , valor = linha.split(' ')
                        for v in variaveis:
                            if v[0] == variavel:
                                v[1] = float(valor)
                                break
                    # modifica o valor de um vetor
                    elif linha.startswith('mdf'):
                        comando, vetor , pos , valor = linha.split(' ')
                        for v in vetores:
                            if v[0] == vetor:
                                if valor.isnumeric():
                                    v[1][f'{pos}'] = float(valor)
                                else:
                                    for l in variaveis:
                                        if l[0] == valor:
                                            v[1][f'{pos}'] = l[1]
                                            break
                                break
                    # copia o valor de um vetor para outro
                    elif linha.startswith('ful'):
                        comando, vetor , vetor2 = linha.split(' ')
                        for v in vetores:
                            if v[0] == vetor:
                                for v1 in vetores:
                                    if v1[0] == vetor2:
                                        v[1] = v1[1]
                    # cria uma variável do tipo float
                    elif linha.startswith('ptf'):
                        comando, nome , valor = linha.split(' ')
                        variaveis.append([nome, float(valor)])
                    # criar um vetor tridimensional
                    elif linha.startswith('3ptf'):
                        comando, nome = linha.split(' ')
                        vetores.append([nome, {'x':0,'y':0,'z':0}])
                    # soma vetores
                    elif linha.startswith('sun'):
                        comando, vetor1, vetor2 = linha.split(' ')
                        for v in vetores:
                            if v[0] == vetor1:
                                for v1 in vetores:
                                    if v1[0] == vetor2:
                                        v[1]['x'] += v1[1]['x']
                                        v[1]['y'] += v1[1]['y']
                                        v[1]['z'] += v1[1]['z']
                                        break
                                break
                    # subtrai vetores
                    elif linha.startswith('sub'):
                        comando, vetor1, vetor2 = linha.split(' ')
                        for v in vetores:
                            if v[0] == vetor1:
                                for v1 in vetores:
                                    if v1[0] == vetor2:
                                        v[1]['x'] -= v1[1]['x']
                                        v[1]['y'] -= v1[1]['y']
                                        v[1]['z'] -= v1[1]['z']
                                        break
                                break
                    # multiplica vetores
                    elif linha.startswith('mulv'):
                        comando, vetor1, vetor2 = linha.split(' ')
                        for v in vetores:
                            if v[0] == vetor1:
                                for v1 in vetores:
                                    if v1[0] == vetor2:
                                        v[1]['x'] *= v1[1]['x']
                                        v[1]['y'] *= v1[1]['y']
                                        v[1]['z'] *= v1[1]['z']
                                        break
                                break
                    # divide vetores
                    elif linha.startswith('div'):
                        comando, vetor1, vetor2 = linha.split(' ')
                        for v in vetores:
                            if v[0] == vetor1:
                                for v1 in vetores:
                                    if v1[0] == vetor2:
                                        v[1]['x'] /= v1[1]['x']
                                        v[1]['y'] /= v1[1]['y']
                                        v[1]['z'] /= v1[1]['z']
                                        break
                                break
                    # atribui o produto escalar de um vetor a uma variável
                    elif linha.startswith('dot'):
                        comando, vetor1, vetor2, var = linha.split(' ')
                        for v in vetores:
                            if v[0] == vetor1:
                                for v1 in vetores:
                                    if v1[0] == vetor2:
                                        dot = 0
                                        dot += v[1]['x'] * v1[1]['x']
                                        dot += v[1]['y'] * v1[1]['y']
                                        dot += v[1]['z'] * v1[1]['z']
                                        for v2 in variaveis:
                                            if v2[0] == var:
                                                v2[1] = dot
                                                break
                                        break
                                break
                    # multiplica um vetor com uma matriz do bdm
                    elif linha.startswith('mulm'):
                        comando, pos_m, vetor1 = linha.split(' ')
                        for v in vetores:
                            if v[0] == vetor1:
                                for pos0, n in enumerate(bdm[f"{pos_m}"]):
                                    soma = 0
                                    for pos1, n1 in enumerate(n):
                                        if pos1 == 0:
                                            soma += n1 * v[1]["x"]
                                        elif pos1 == 1:
                                            soma += n1 * v[1]["y"]
                                        elif pos1 == 2:
                                            soma += n1 * v[1]["z"]
                                    if pos0 == 0:
                                        v[1]["x"] = soma
                                    elif pos0 == 1:
                                        v[1]['y'] = soma
                                    elif pos0 == 2:
                                        v[1]['z'] = soma
                                break
                    linha = ''
    for v in vetores:
        if v[0] == 'vecO':
            vertice_saida.append(v[1]['x'])
            vertice_saida.append(v[1]['y'])
            vertice_saida.append(v[1]['z'])
            break
    return vertice_saida