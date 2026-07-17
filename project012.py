from datetime import date
n1 = int(input(' em que ano você nasceu:'))
nome = input('digite seu sexo:').capitalize()
n3 = date.today().year
n4 = n3 - n1
if n4 < 18 and nome == 'Masculino':
    print('ainda não pode se alistar ao exercito mas daqui a {} anos você ira se alistar ao exercito '.format(n4 - 18))
elif n4 == 18:
    print('esta na hora de se alistar')
elif n4 > 18:
    print('deveria ter se alistado a {} anos'.format(n4 - 18))
else:
    print('não e preciso que se aliste')