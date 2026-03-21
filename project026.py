frase = str(input('escreva uma frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]
if inverso == junto:
    print('esta frase e um palindromo')
else:
    print('esta frase não e um palindromo')

