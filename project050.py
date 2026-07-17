palavras = ('ola','mais','oque','cola','saber',
            'aprender','progamar','como','ate')
for c in palavras:
    print(f'\nna palavra {c.upper()} temos ',end = ' ')
    for letra in c:
        if letra in 'aeiou':
            print(letra,end = ' ')
