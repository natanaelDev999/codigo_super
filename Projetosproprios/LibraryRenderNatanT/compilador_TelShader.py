
def compila_codigo_TelShader(codigo_TelShader,pixel,x,y):
    pixel_saida = ' '
    linha = ''
    x1 = x
    y1 = y
    variaveis = []
    for c in codigo_TelShader:
        if c != ';':
            linha += c
        else:
            linha = linha.strip()
            if linha.startswith('p=') or linha.startswith('p ='):
                vars,chr = linha.split('=')
                if chr == 'pr':
                    pixel_saida = pixel
                else:
                    pixel_saida = chr
            elif linha.startswith('cp=') or linha.startswith('cp ='):
                vars,chr = linha.split('=')
                r,g,b = chr.split(',')
                pixel_saida = f'\033[38;2;{r};{g};{b}m{pixel_saida}\033[m'
            elif linha.startswith('x=') or linha.startswith('x ='):
                vars,pos = linha.split('=')
                if pos.isnumeric():
                    x1 = int(pos)
                else:
                    for i in variaveis:
                        if i[0] == pos:
                            x1 = i[1]
                            break
            elif linha.startswith('y=') or linha.startswith('y ='):
                vars,pos = linha.split('=')
                if pos.isnumeric():
                    y1 = int(pos)
                else:
                    for i in variaveis:
                        if i[0] == pos:
                            y1 = i[1]
            elif linha.startswith('v'):
                operacao, valor1, valor2 = linha.split(' ')
                if valor1 == 'x':
                    if valor2.isnumeric():
                        x1 += float(valor2)
                    else:
                        for i in variaveis:
                            if i[0] == valor2:
                                x1 += i[1]
                elif valor1 == 'y':
                    if valor2.isnumeric():
                        y1 += float(valor2)
                    else:
                        for i in variaveis:
                            if i[0] == valor2:
                                y1 += i[1]
            elif linha.startswith('s'):
                operacao, valor1, valor2 = linha.split(' ')
                if valor1 == 'x':
                    if valor2.isnumeric():
                        x1 -= float(valor2)
                    else:
                        for i in variaveis:
                            if i[0] == valor2:
                                x1 -= i[1]
                elif valor1 == 'y':
                    if valor2.isnumeric():
                        y1 -= float(valor2)
                    else:
                        for i in variaveis:
                            if i[0] == valor2:
                                y1 -= i[1]
            elif linha.startswith('ptf'):
                comando, nome , valor = linha.split(' ')
                variaveis.append([nome,float(valor)])
            linha = ''
    return [pixel_saida,int(x1),int(y1)]