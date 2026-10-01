
#                           TelMatrixShader
#A linguagem de vértice do terminal
def compila_codigo_telmatrixshader(codigo_TelMatrixShader, vertice):
    vertice_saida = []
    # vetores
    vetores = [['vecI',{'x':vertice[0],'y':vertice[1],'z':vertice[2]}],['vecO',{'x':0,'y':0,'z':0}]]
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
                        v[1][f'{pos}'] = float(valor)
                        break
            if linha.startswith('ful'):
                comando, vetor , vetor2 = linha.split(' ')
                for v in vetores:
                    if v[0] == vetor:
                        for v1 in vetores:
                            if v1[0] == vetor2:
                                v[1] = v1[1]
    for v in vetores:
        if v[0] == 'vecO':
            vertice_saida.append(v[1]['x'])
            vertice_saida.append(v[1]['y'])
            vertice_saida.append(v[1]['z'])
            break
    return vertice_saida