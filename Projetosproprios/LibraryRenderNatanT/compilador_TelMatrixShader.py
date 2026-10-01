
#                           TelMatrixShader
#A linguagem de vértice do terminal
def compila_codigo_telmatrixshader(codigo_TelMatrixShader, vertice):
    vertice_saida = []
    # vetores
    vetores = [['vecI',{'x':vertice[0],'y':vertice[1],'z':vertice[2]}],['vecO',{'x':0,'y':0,'z':0}]]
    # variáveis
    variaveis = []
    # lê código
    linha = ''
    for c in codigo_TelMatrixShader:
        if c != ';':
            linha += c
        else:
            linha = linha.strip()
            if linha.startswith('mdf'):
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
            elif linha.startswith('ful'):
                comando, vetor , vetor2 = linha.split(' ')
                for v in vetores:
                    if v[0] == vetor:
                        for v1 in vetores:
                            if v1[0] == vetor2:
                                v[1] = v1[1]
            elif linha.startswith('ptf'):
                comando, nome , valor = linha.split(' ')
                variaveis.append([nome, float(valor)])
            elif linha.startswith('3ptf'):
                comando, nome = linha.split(' ')
                vetores.append([nome, {'x':0,'y':0,'z':0}])
            linha = ''
    for v in vetores:
        if v[0] == 'vecO':
            vertice_saida.append(v[1]['x'])
            vertice_saida.append(v[1]['y'])
            vertice_saida.append(v[1]['z'])
            break
    print(vetores)
    return vertice_saida