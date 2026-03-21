p1 = int(input('escreva o primeiro termo:'))
r = int(input('escreva a razão:'))
d = p1 + (10 - 1)* r
for c in range(p1, d + r, r):
    print('{}'.format(c))