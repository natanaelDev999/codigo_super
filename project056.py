expressao = input('digite uma expressão:')
parenteses1 = list()
parenteses2 = list()
for l in expressao:
    if l == '(':
        parenteses1.append(l)
    elif l == ')':
        parenteses2.append(l)
if len(parenteses1) == len(parenteses2):
    print('expressão correta')
else:
    print('expressão incorreta')
