def metade(v):
    return v // 2
def dobro(v):
    return v * 2
def aumentar(v,m):
    return ((v*m)//100) + v
def diminuir(v,m):
    return v - ((v*m)//100)
def moeda(v,sit):
    if sit == True:
        return f'R${v:.2f}'.replace('.',',')
    else:
        return v
