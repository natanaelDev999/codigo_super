def area(a,l):
    area = a * l
    print(f'a area de um terreno {a} x {l} é de {area}m²')
print('     controle de terrenos')
print('-'*30)
num1 = float(input('escreva a largura (m): '))
num2 = float(input('escreva o comprimento (m): '))
area(num1,num2)
