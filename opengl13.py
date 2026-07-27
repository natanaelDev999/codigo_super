import glfw
import math
from OpenGL.GL import *
from OpenGL.GLU import *
#Para criar um contexto OpenGl glfw.make_context_current(window);Manter a janela not glfw.window_should_close(window)
#Para detectar eventos glfw.poll_events();Para parar o loop utilize glfw.wait_events;Para manter a janela glfw.swap_buffers(window)
#Para escolher a cor do fundo  OpenGL.GL.glClearColor(0,0,0,0);Para aplicar a cor glClear(GL_COLOR_BUFFER_BIT)
x = 0
y = -0.25
z = -1
angle = 0
# Trata da cor
angulo = 0
def init():
    glClearColor(1,1,1,1)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, 1, 0.1, 50)
    glMatrixMode(GL_MODELVIEW)
def render():
    glLoadIdentity()
    glRotatef(angle, 0, 1, 0)
    glTranslatef(x, y, z)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)
    glBegin(GL_TRIANGLES)
    # esquerda
    glVertex3f(-0.03 * math.cos(math.radians(angulo)),-0.03,-0.03*math.sin(math.radians(angulo)))
    # direita
    glVertex3f(0.03 * math.cos(math.radians(angulo)),-0.03,-0.03*math.sin(math.radians(angulo)))
    # cima
    glVertex3f(0.03 * math.cos(math.radians(angulo)),0.03,-0.03*math.sin(math.radians(angulo)))
    glEnd()
    glBegin(GL_TRIANGLES)
    # esquerda
    glVertex3f(-0.03 * math.cos(math.radians(angulo)), 0.03, -0.03 * math.sin(math.radians(angulo)))
    # direita
    glVertex3f(-0.03 * math.cos(math.radians(angulo)), -0.03, -0.03 * math.sin(math.radians(angulo)))
    # cima
    glVertex3f(0.03 * math.cos(math.radians(angulo)), 0.03, -0.03 * math.sin(math.radians(angulo)))
    glEnd()

    glBegin(GL_TRIANGLES)
    # esquerda
    glVertex3f(-0.03 * math.cos(math.radians(angulo)), -0.03, -0.09 * math.sin(math.radians(angulo)))
    # direita
    glVertex3f(0.03 * math.cos(math.radians(angulo)), -0.03, -0.09 * math.sin(math.radians(angulo)))
    # cima
    glVertex3f(0.03 * math.cos(math.radians(angulo)), 0.03, -0.09 * math.sin(math.radians(angulo)))
    glEnd()
    glBegin(GL_TRIANGLES)
    # esquerda
    glVertex3f(-0.03 * math.cos(math.radians(angulo)), 0.03, -0.09 * math.sin(math.radians(angulo)))
    # direita
    glVertex3f(-0.03 * math.cos(math.radians(angulo)), -0.03, -0.09 * math.sin(math.radians(angulo)))
    # cima
    glVertex3f(0.03 * math.cos(math.radians(angulo)), 0.03, -0.09 * math.sin(math.radians(angulo)))
    glEnd()


def main():
    global angulo
    glfw.init()
    window = glfw.create_window(700,700,"window - 13",None,None)
    glfw.make_context_current(window)
    init()
    while not glfw.window_should_close(window):
        render()
        glfw.poll_events()
        glfw.swap_buffers(window)
        angulo += 0.25
    glfw.terminate()
main()