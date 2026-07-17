numeros = [[],[]]
for c in range(0,7):
    num = int(input('digite um numero:'))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print(numeros)
print(f'estes são os numeros pares em ordem crescente: {numeros[0]}')
print(f'estes são os numeros impares em ordem crescente: {numeros[1]}')
