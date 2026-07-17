primeiro = int(input('primeiro termo:'))
razao = int(input('razão da PA:'))
termo = primeiro
cont = 1
num = 0
mais = 10
while mais != 0:
    num += mais
    while cont <= num:
        print(' {} '. format(termo), end = '')
        termo += razao
        cont += 1
    print('pausa')
    mais = int(input('quantos termos você quer mostrar a mais '))
print('progeção finalizada com {} termos escreitos '.format(num))

