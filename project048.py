n1 = int(input('escreva um numero:'))
n2 = int(input('escreva um numero:'))
n3 = int(input('escreva um numero:'))
n4 = int(input('escreva um numero:'))
t = (n1,n2,n3,n4)
print(f'voce escreveu os numeros {t}')
print(f'o valor nove apareceu {t.count(9)} vezes')
if 3 in t:
    print(f'o numero 3 apareceu {t.index(3)}')
else:
    print('o numero 3 não apareceu')
'''n = 0
q = 0
for x in t:
    if 9 == t[n]:
        q += 1
    n += 1
    if n == 5:
        break
print(f'você escreveu {q} vezes o nove')
n2 = 0
p3 = 0
for x in t:
    if 3 == t[n2]:
        p3 = t.index(3)
        print(f'o primeiro valor 3 esta na posição {p3 + 1}')
    n2 += 1
if p3 == 0:
    print('o valor tres não foi digitado em nenhuma posição')'''
n3 = 0
pares = 0
cont = 0
for x in t:
    if t[n3] % 2 == 0:
        pares = t[n3]
        cont += 1
        if cont == 1:
            print(f'os valores pares são {pares}', end = ' ')
    if cont >= 2:
        print(f'{pares}', end = ' ')
    n3 += 1



