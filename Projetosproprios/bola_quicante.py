'''import os
import time
matrix = [['  ','  ','  ','+ '],
          ['  ','  ','  ','  '],
          ['  ','  ','  ','  '],
          ['+','  ','  ','  ']]
x = 0
y = 0
for c in range(0,4):
    matrix[y][x] = ' '
    if c > 0:
        y += 1
        x += 1
    print(f'posição: x = {x}; y = {y}')
    matrix[y][x] = 'o'
    for linha in matrix:
        for coluna in linha:
            print(coluna,end=' ')
        print()
    time.sleep(1)
    os.system('cls')'''
