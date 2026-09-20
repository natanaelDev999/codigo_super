
def compila_codigo_TelShader(codigo_TelShader,pixel):
    pixel_saida = ' '
    linha = ''
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
            linha = ''
    return pixel_saida