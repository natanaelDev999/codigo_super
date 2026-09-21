
def compila_codigo_TelShader(codigo_TelShader,pixel,x,y):
    pixel_saida = ' '
    linha = ''
    x1 = x
    y1 = y
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
                x1 = int(pos)
            elif linha.startswith('y=') or linha.startswith('y ='):
                vars,pos = linha.split('=')
                y1 = int(pos)
            elif linha.startswith('v'):
                operacao, valor1, valor2 = linha.split(' ')
                if valor1 == 'x':
                    x1 += float(valor2)
                elif valor1 == 'y':
                    y1 += float(valor2)
            linha = ''
    return [pixel_saida,int(x1),int(y1)]