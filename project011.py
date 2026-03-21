n1 = int(input('escreva um numero:'))
n2 = int(input('escreva outro numero:'))
if n1 > n2:
    print('o {} e maior que {}'.format(n1, n2))
elif n1 < n2:
    print('o {} e maior que {}'.format(n2, n1))
elif n1 == n2:
    print('o {} e igual a {}'.format(n1 , n2))