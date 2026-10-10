# entradas
entradas = [-3,5]
# saídas
saidas = [0,1]
# resultado
resultado = 0
# lista de neurônios
neuronios = [{'entradas':[entradas[0],entradas[1]],'distancias':[.2,.5],'bias':2},
             {'entradas':[entradas[0],entradas[1]],'distancias':[.5,.2],'bias':1.5}]
# estrutura do neurônio: entradas ; distâncias ; bias ; saída.
# cálcula a saída
def calcula_saida():
    global neuronios, saidas , resultado
    resul = 0
    saida = 0
    # consegue o resultado
    for n in neuronios:
        soma_d = 0
        soma_e = 0
        for c in n['distancias']:
            soma_d += c
        for c2 in n['entradas']:
            soma_e += c2
        resul = soma_d * soma_e + n['bias']
    # verifica a saída correta
    if resul < 0:
        resul = 0
    for pos0,s in enumerate(saidas):
        if s-resul != 0 or resul < s:
            resultado = pos0

# função principal
def main():
    calcula_saida()
    print('Posição: ',resultado,', Valor', saidas[resultado])
main()