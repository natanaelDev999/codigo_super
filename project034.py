from math import factorial
n1 = int(input('escreva um numero e saiba seu fatorial:'))
c = n1
f = factorial(n1)
print('cauculando fatorial {}! = '.format(n1), end = '')
while c > 0:
    print(f'{c}', end = '')
    print(' x ' if c > 1 else ' = {}'.format(f), end = '')
    c -= 1
