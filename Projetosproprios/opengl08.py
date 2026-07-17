import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
x = 0
y = 0
z = -5
angle = 0
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
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINES)
    for c in obj:
        glVertex3fv(c)
    glEnd()
def main():
    glfw.init()
    window = glfw.create_window(600,600,"SuperSpace 2",None,None)
    glfw.make_context_current(window)
    init()
    while not glfw.window_should_close(window):
        render()
        glfw.poll_events()
        glfw.swap_buffers(window)
    glfw.terminate()
main()