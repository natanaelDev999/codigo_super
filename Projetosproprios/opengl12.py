import math
import glfw
from OpenGL.GL import *

angle = 0

def init():
    glClearColor(0,0,0,0)

def render():
    global angle
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)
    glBegin(GL_TRIANGLES)
    # esquerda
    glVertex2f(-0.03 * math.cos(angle) - -0.03 * math.sin(angle), -0.03 * math.sin(angle) + -0.03 * math.cos(angle))
    # direita
    glVertex2f(0.03 * math.cos(angle) - -0.03 * math.sin(angle), 0.03 * math.sin(angle) + -0.03 * math.cos(angle))
    # cima
    glVertex2f(0.03 * math.cos(angle) - 0.03 * math.sin(angle), 0.03 * math.sin(angle) + 0.03 * math.cos(angle))
    glEnd()
    glBegin(GL_TRIANGLES)
    # esquerda
    glVertex2f(-0.03 * math.cos(angle) - 0.03 * math.sin(angle), -0.03 * math.sin(angle) + 0.03 * math.cos(angle))
    # direita
    glVertex2f(-0.03 * math.cos(angle) - -0.03 * math.sin(angle), -0.03 * math.sin(angle) + -0.03 * math.cos(angle))
    # cima
    glVertex2f(0.03 * math.cos(angle) - 0.03 * math.sin(angle), 0.03 * math.sin(angle) + 0.03 * math.cos(angle))
    glEnd()

def main():
    global angle
    glfw.init()
    window = glfw.create_window(700,700,"window - 12",None,None)
    glfw.make_context_current(window)
    init()
    while not glfw.window_should_close(window):
        render()
        glfw.poll_events()
        glfw.swap_buffers(window)
        angle += 0.0005
    glfw.terminate()
main()