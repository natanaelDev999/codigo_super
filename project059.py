lista = [[],[],[]]
for c in range(0, 3):
    for v in range(0, 3):
        num = (int(input(f'digite um numero para [{c},{v}]: ')))
        lista[c].append(num)
for l in lista:
    print(f'[{l[0]:^5}][{l[1]:^5}][{l[2]:^5}]')