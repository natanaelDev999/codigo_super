n1 = float(input('escreva o tamanho do primeira reta:'))
n2 = float(input('escreva o tamanho da segunda reta:'))
n3 = float(input('escreva o tamanho da terceira reta:'))
if n1 < n2 + n3 or n2 < n1 + n3 or n3 < n1 + n2:
    print('e possivel criar um triangulo', end = '')
    if n1 == n2 == n3:
        print(' equilatero com essas retas')
    elif n1 != n2 == n3 or n2 != n1 == n3 or n3 != n1 == n2:
        print(' isosceles com estas retas')
    else:
        print(' escaleano com essas retas')
else:
    print('não e possivel criar nenhum tipo de triangulo')