lista = [[],[],[]]
pares = 0
for c in range(0,3):
    for v in range(0,3):
        num = int(input(f'digite um numero para [{c},{v}]: '))
        if num % 2 == 0:
            pares += num
        lista[c].append(num)
for l in lista:
    print(f'[{l[0]:^5}][{l[1]:^5}][{l[2]:^5}]')
print(f'a soma dos valores pares e {pares}')
soma = lista[0][2] + lista[1][2] + lista[2][2]
print(f'a soma dos numeros da terceira coluna e {soma}' )
print(f'o maior numero da 2ª linha e {max(lista[1])}')