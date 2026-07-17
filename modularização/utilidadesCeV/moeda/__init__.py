def dobro(num,form):
    if form == False:
        return num*2
    elif form == True:
        return f'R${num*2:.2f}'.replace('.',',')
def metade(num,form):
    if form == False:
        return num/2
    elif form == True:
        return f'R${num/2:.2f}'.replace('.',',')
def mais(num,mais,form):
    if form == False:
        return (num*mais)/100+num
    elif form == True:
        return f'R${(num*mais)/100+num:.2f}'.replace('.',',')
def menos(num,menos,form):
    if form == False:
        return (num * mais) / 100 - num
    elif form == True:
        return f'R${num-(num * menos) / 100:.2f}'.replace('.', ',')
def moeda(num):
    return f'R${num:.2f}'.replace('.',',')
def linha():
    print('-'*30)
def resumo(num,me,ma):
    linha()
    print('      RESUMO DO VALOR     ')
    linha()
    print(f'Preço analisado:    {moeda(num)}')
    print(f'Dobro do preço:     {dobro(num,True)}')
    print(f'Metade do preço:    {metade(num,True)}')
    print(f'{ma}% de aumento:     {mais(num,ma,True)}')
    print(f'{me}% de redução:     {menos(num,me,True)}')
    linha()