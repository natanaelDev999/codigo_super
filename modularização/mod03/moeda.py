def dobro(num,form):
    if form == False:
        return num*2
    elif form == True:
        return f'R${num*2:.2f}'.replace('.',',')
def metade(num,form):
    if form == False:
        return form//2
    elif form == True:
        return f'R${num//2:.2f}'.replace('.',',')
def mais(num,mais,form):
    if form == False:
        return (num*mais)/100+num
    elif form == True:
        return f'R${(num*mais)/100+num:.2f}'.replace('.',',')
def menos(num,menos,form):
    if form == False:
        return (num * mais) / 100 + num
    elif form == True:
        return f'R${num-(num * menos) / 100:.2f}'.replace('.', ',')
def moeda(num):
    return f'R${num:.2f}'.replace('.',',')