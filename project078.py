def mostradoc():
    while True:
        print(f'\033[0;0;42m{"~"*30}\033[m\n\033[0;0;42m   SISTEMA DE AJUDA PYhelp    \033[m\n\033[0;0;42m{"~"*30}\033[m')
        func = str(input('Função ou biblioteca > '))
        if not func == 'fim':
            doc = str(help(func))
            print(f'\033[0;0;0m{doc}\033[m')
        else:
            print(f'\033[0;0;41m{"~"*15}\033[m\n\033[0;0;41m    ATÉ LOGO   \033[m\n\033[0;0;41m{"~"*15}\033[m')
            break
mostradoc()