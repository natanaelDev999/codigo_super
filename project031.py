t = True
while t == True:
    sexo = str(input('escreva o sexo de uma pessoa: M/F')).upper().strip()[0]
    if sexo == 'M' or sexo == 'F':
        print(f'dado armazenado sexo:{sexo}')
        t = False
    else:
        print('dado não armazenado por ser invalido')
print('pronto')
