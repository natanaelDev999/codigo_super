from pynput.mouse import Button, Controller
import os
import time
'''mouse = Controller()
time.sleep(4)
#mouse.position = (x,y) leva para o lugar selecionado
#mouse.move(500,300) move para o local selecionado
#mouse.click(Button.botão, quant=1) clica no botão selecionado
#mouse.press(Button.botao) pressiona o botal selecionado
print(mouse.position) mostra a posição
#'''
from pynput.mouse import Listener
print(f' {"_"*12}\n|botão do ola|\n {"-"*12}')
def clique(x, y, button, pressed):
    os.system('cls')
    if pressed and button == Button.left and x >= 70 and y >= 490:
        print(f' {"_" * 8}\n|obrigado|\n {"-" * 8}')
        time.sleep(1)
        os.system('cls')
        print(f"ola")
        return False
# Começa a ouvir o mouse
with Listener(on_click=clique) as listener:
    listener.join()