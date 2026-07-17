import glfw
from OpenGL.GL import *

verticies = [[-0.8,-0.4],
             [-0.8,0.4],
             [-0.4,-0.8],
             [-0.4,0.8],
             [0.4,-0.8],
             [0.4,0.8],
             [0.8,-0.4],
             [0.8,0.4]]

def init():
    glClearColor(1,1,1,1)
    glPointSize(5)
    glLineWidth(4)

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 0, 2)
    glBegin(GL_POINTS)
    for v in verticies:
        glVertex2fv(v)
    glEnd()

    glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)
    glBegin(GL_TRIANGLE_STRIP)
    for v2 in verticies:
        glVertex2fv(v2)
    glEnd()

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glColor3f(0,0,0)
    glBegin(GL_TRIANGLE_STRIP)
    for v2 in verticies:
        glVertex2fv(v2)
    glEnd()
def main():
    glfw.init()
    window = glfw.create_window(600,600,"primitivas",None,None)
    glfw.make_context_current(window)
    init()
    while not glfw.window_should_close(window):
        render()
        glfw.poll_events()
        glfw.swap_buffers(window)
    glfw.terminate()
main()