n1 = float(input('digite o tamanho de uma reta :'))
n2 = float(input('digite o tamanho de outra reta:'))
n3 = float(input('digite o tamanho de outra reta:'))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('com essas retas e possivel criar um triangulo')
else:
    print('não e possivel fazer um triângulo com essas retas ')