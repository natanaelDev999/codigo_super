from datetime import date
n1 = int(input('qual o ano de nascimento do atleta:'))
n2 = date.today().year
n3 = n2 - n1
if n3 <=9:
    print('este atleta esta na categoria de \033[35mmirin\033[m')
elif n3 <= 14:
    print('este atleta esta na categoria de \033[35minfantil\033[m')
elif n3 <= 19:
    print('este atleta esta na categoria de \033[35mjunior\033[m')
elif n3 <= 25:
    print('este atleta esta na categoria de \033[35msenior\033[m')
elif n3 >=26:
    print('este atleta esta na categoria de \033[31mmaster\033[m')