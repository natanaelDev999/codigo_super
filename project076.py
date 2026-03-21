def inputint(palavra):
    n = ''
    while not n.isnumeric():
        n = input(palavra)
        if n.isnumeric():
            break
        else:
            print('POR FAVOR DIGITE UM NUMERO')

    return int(n)
n = inputint('escreva um numero:')
print(f'o numero registrado foi {n}')

