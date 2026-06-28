import glfw
import math
import random
from OpenGL.GL import *
from OpenGL.GLU import *
x = 0
y = 0
z = -5
angle = 0
def cria_esfera(raio):
    vertices = []

    for i in range(30+1):
        phi = math.pi * i / 30

        for j in range(30+1):
            theta = 2 *math.pi * j / 30

            x2 = raio * math.sin(phi) * math.cos(theta)
            y2 = raio * math.cos(phi)
            z2 = raio * math.sin(phi)* math.sin(theta)

            vertices.append([x2+random.randint(0,60)/100,
                             y2+random.randint(0,60)/100,
                             z2+random.randint(0,60)/100])
    return vertices
def init():
    glClearColor(0,0,0.4,0)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, 1, 0.1, 500000000000000000000000)
    glMatrixMode(GL_MODELVIEW)
    glPointSize(5)
def render():
    global x,y,z
    glLoadIdentity()
    glRotatef(angle, 0, 1, 0)
    glTranslatef(x, y, z)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glTranslatef(0, 0, -65)
    glColor3f(1,1,0)
    esf = cria_esfera(15)
    glBegin(GL_QUADS)
    for c in range(30):
        for v in range(30):
            ponto1 = c * (30+1) + v
            ponto2 = ponto1 + 1
            ponto3 = (c+1)*(30+1)+v+1
            ponto4 = (c + 1) * (30 + 1) + v

            glVertex3fv(esf[ponto1])
            glVertex3fv(esf[ponto2])
            glVertex3fv(esf[ponto3])
            glVertex3fv(esf[ponto4])
    glEnd()

def main():
    glfw.init()
    window = glfw.create_window(800,800,"Teste planeta",None,None)
    glfw.make_context_current(window)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    init()
    while not glfw.window_should_close(window):
        render()
        glfw.poll_events()
        glfw.swap_buffers(window)
    glfw.terminate()
main()