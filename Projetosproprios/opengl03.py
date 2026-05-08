import glfw
from OpenGL.GL import *
import time
dados = []
#Para criar um contexto OpenGl glfw.make_context_current(window);Manter a janela not glfw.window_should_close(window)
#Para detectar eventos glfw.poll_events();Para parar o loop utilize glfw.wait_events;Para manter a janela glfw.swap_buffers(window)
#Para escolher a cor do fundo  OpenGL.GL.glClearColor(0,0,0,0);Para aplicar a cor glClear(GL_COLOR_BUFFER_BIT)

# Trata da cor
def init():
    glClearColor(0,0,0,0)
quant = 0
def render():
    global quant
    #if quant <= 1:
    time.sleep(0.05)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)
    glBegin(GL_TRIANGLES)
    # esquerda
    glVertex2f(-0.3+(quant/2), -0.3 - quant)
    # direita
    glVertex2f(0.3-(quant/2), -0.3)
    # cima
    glVertex2f(0.3-(quant/2), 0.3)
    glEnd()
    #
    glColor3f(1, 0, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.3+(quant/2), 0.3 + quant)
    glVertex2f(-0.3+(quant/2), -0.3 - quant)
    glVertex2f(0.3-(quant/2), 0.3)
    glEnd()
    '''elif quant > 1:
        time.sleep(0.05)
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1, 0, 0)
        glBegin(GL_TRIANGLES)
        # esquerda
        glVertex2f(-0.3, -0.3)
        # direita
        glVertex2f(0.3, -0.3)
        # cima
        glVertex2f(0.3, 0.3)
        glEnd()
        #
        glColor3f(1, 0, 0)
        glBegin(GL_TRIANGLES)
        glVertex2f(-0.3, 0.3)
        glVertex2f(-0.3, -0.3)
        glVertex2f(0.3, 0.3)
        glEnd()
        quant = 0'''
def analise():
    print(f'lista de dados:menor ângulo:{min(dados):.2f};maior ângulo:{max(dados)};metade do ângulo maior:{max(dados)/2:.2f}')
# Função principal
def main():
    global quant
    global dados
    glfw.init()
    window = glfw.create_window(700,700,"window - 01",None,None)
    glfw.make_context_current(window)
    init()
    while not glfw.window_should_close(window):
        render()
        glfw.poll_events()
        glfw.swap_buffers(window)
        quant += 0.01
        dados.append(quant)
    glfw.terminate()
    analise()
main()