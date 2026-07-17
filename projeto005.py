from random import randint
n1 = randint(1, 5)
print('escolhi um numero entre 0 a 5 adivinhe qual e')
n3 = int(input('escreva o numero que acha que e :'))
if n1 == n3:
    print('parabens acertou :)!!!')
else:
    print('a errou eu escolhi o {} aposto que ira melhorar'.format(n1))
