numeros = list()
for i in range(0,5):
    numeros.append(int(input(f'digite o valor da posição {i}:')))
maior = max(numeros)
menor = min(numeros)
print(f'você digitou os numeros: {numeros}')
print(f'o maior e {maior} na posição {numeros.index(maior)}')
print(f'o menor e {menor} na posição {numeros.index(menor)}')