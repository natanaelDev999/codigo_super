etxt = input('>>> ')
def parenteses(txt):
    if '(' in txt and ')' in txt:
        loc = txt.index('(')
        loc2 = txt.index(')')
        if txt[:loc].strip() == 'write >>':
            txtsel = txt[loc+1:loc2]
            if len(txtsel) > 0:
                print(f'Saida:\n{txtsel}')
            else:
                print('Não há nada no interior dos parenteses')
        else:
            print('Comando invalido')
    else:
        print('Comando invalido por não conter parenteses!')
parenteses(etxt)
