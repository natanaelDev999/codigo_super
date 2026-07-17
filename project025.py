n1 = int(input('escreva um numero:'))
t = 0
for c in range(1, n1+ 1):
    if  n1 % c == 0:
        print('\033[34m',end ='')
        t += 1
    else:
        print('\033[m', end = '')
    print(' {} '.format(c), end = '')
print('\n\033[mo numero  {} foi divizivel {} vezes'.format(n1, t))
if t == 2:
    print('o numero e PRIMO')
else:
    print('o numero NÃO e primo')
