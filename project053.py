numeros = []
for c in range(0,5):
    num = int(input('digite um numero:'))
    if c == 0 or num > numeros[-1]:
        numeros.append(num)
    else:
        pos = 0
        while pos < len(numeros):
            if num <= numeros[pos]:
                numeros.insert(pos, num)
                break
            pos += 1
for num in numeros:
    print(numeros)

