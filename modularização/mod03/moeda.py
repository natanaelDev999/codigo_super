def dobro(num,form):
    if form == False:
        return num*2
    elif form == True:
        return moeda(num*2)
def metade(num,form):
    if form == False:
        return num/2
    elif form == True:
        return moeda(num/2)
def mais(num,mais,form):
    if form == False:
        return (num*mais)/100+num
    elif form == True:
        return moeda((num*mais)/100+num)
def menos(num,menos,form):
    if form == False:
        return (num-(num * menos) / 100)
    elif form == True:
        return moeda(num-(num * menos) / 100)
def moeda(num):
    return f'R${num:.2f}'.replace('.',',')