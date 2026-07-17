n1 = int(input('digite um numero:'))
print('''escolha uma opição:
1 para binaro
2 para octal
3 para hexadecimal''')
n2 = int(input('digite sua opição:'))
if n2 == 1:
    print('{} convertido para binario fica {}'.format(n1, bin(n1)[2:]))
elif n2 == 2:
    print('{} convertido em octal fica {}'.format(n1, oct(n1)[2:]))
elif n2 == 3:
    print('{} convertido em haxadecimal fica {}'.format(n1, hex(n1)[2:]))
else:
    print('opição invalida')