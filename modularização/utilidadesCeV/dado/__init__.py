def leiadinheiro():
    while True:
        valor = input('Escreva algum valor de dinheiro: R$')
        if valor.isnumeric():
            return float(valor)
        elif valor.split('.')[0].isnumeric() and valor.split('.')[1].isnumeric():
            return float(valor)
        elif ',' in valor:
            return float(valor.replace(',','.'))
        elif valor.isalpha() or valor.strip() == '':
            print(f"\033[31mO valor '{str(valor)}' é inválido por não tratar-se de um valor monetário\033[m")
        else:
            print(f"\033[31mO valor '{str(valor)}' é inválido por não tratar-se de um valor monetário\033[m")