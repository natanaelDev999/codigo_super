def dobro(num,form):
    if form == False:
        return num*2
    elif form == True:
        return moeda(num)
def metade(num,form):
    if form == False:
        return num//2
    elif form == True:
        return moeda(num)
def mais(num,mais,form):
    if form == False:
        return (num*mais)/100+num
    elif form == True:
        return moeda(num)
def menos(num,menos,form):
    if form == False:
        return (num * mais) / 100 + num
    elif form == True:
        return moeda(num)
def moeda(num):
    return f'R${num:.2f}'.replace('.',',')