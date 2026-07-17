n1 = float(input('escreva sua altura em metros:'))
n2 = float(input('escreva seu peso em quilogramas:'))
n3 = n2 / (n1 ** 2)
print('seu imc e de {:.1f}'.format(n3))
if n3 < 18.5:
    print('o paciente esta abaixo do peso segundo o IMC')
elif n3 >= 18.5 and n3 < 25:
    print('o paciente esta com o peso ideal segundo o IMC')
elif n3 > 25 and n3 < 30:
    print('o paciente esta sobre o peso segundo o IMC')
elif n3 > 30 and n3 < 40:
    print('o paciente esta com obesidade segundo o IMC')
elif n3 > 40:
    print('o paciente esta com obesidade morbida segundo o IMC')