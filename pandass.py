'''import glfw
from OpenGL.GL import *

# inicia glfw
if not glfw.init():
    raise Exception("GLFW não iniciou")

# cria janela
window = glfw.create_window(800, 600, "OpenGL com GLFW", None, None)

if not window:
    glfw.terminate()
    raise Exception("Janela não criada")

glfw.make_context_current(window)

# loop principal
while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)

    # desenha triângulo
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 0.20)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glEnd()

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()'''
