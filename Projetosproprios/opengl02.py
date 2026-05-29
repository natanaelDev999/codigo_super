import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
x = 0
y = 0
z = -5
angle = 0
def key_callback(window, key, scancode, action, mods):
    global verticies,x,y,z,angle
    #
    # if key == glfw.KEY_A and action == glfw.PRESS:
    #     x += 0.5
    # if key == glfw.KEY_D and action == glfw.PRESS:
    #      x -= 0.5
    if key == glfw.KEY_W:
        z += 0.5
    if key == glfw.KEY_S:
        z -= 0.5
    if key == glfw.KEY_A:
        angle -= 4
        print(angle)
    elif key == glfw.KEY_D:
        angle += 4
        print(angle)

verticies = [[-0.5,0.5,0.0],[0.5,0.5,0.0],[-0.5,-0.5,0.0],
             [0.5,0.5,0.0],[-0.5,-0.5,0.0],[0.5,-0.5,0.0],
             [-0.5,0.5,1.001],[0.5,0.5,1.001],[-0.5,-0.5,1.001],
             [0.5,0.5,1.001],[-0.5,-0.5,1.001],[0.5,-0.5,1.001],
             [-0.5,0.5,0.0],[-0.5,0.5,1],[-0.5,-0.5,1],
             [-0.5,0.5,0.0],[-0.5,-0.5,1],[-0.5,-0.5,0.0],
             [0.5,-0.5,0.0],[0.5,-0.5,1],[0.5,0.5,1],
             [0.5,-0.5,0.0],[0.5,0.5,1],[0.5,0.5,0.0],
             [-0.5,0.5,0.0],[-0.5,0.5,1],[0.5,0.5,1],
             [0.5,-0.5,0.0],[0.5,-0.5,1],[-0.5,-0.5,1]]
def init():
    glClearColor(0,0,0,0)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, 1, 0.1, 50)
    glMatrixMode(GL_MODELVIEW)
def render():
    global x,y,z
    glLoadIdentity()
    glRotatef(angle, 0, 1, 0)
    glTranslatef(x, y, z)
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINE_LOOP)
    glColor3f(1,1,1)
    for pos,obj in enumerate(verticies):
        if pos <= 2:
            glVertex3fv(obj)
    glEnd()

    glBegin(GL_LINE_LOOP)
    for pos, obj in enumerate(verticies):
        if pos <= 5 and pos > 2:
            glVertex3fv(obj)
    glEnd()

    glBegin(GL_LINE_LOOP)
    for pos, obj in enumerate(verticies):
        if pos <= 8 and pos > 5:
            glVertex3fv(obj)
    glEnd()

    glBegin(GL_LINE_LOOP)
    for pos, obj in enumerate(verticies):
        if pos <= 11 and pos > 8:
            glVertex3fv(obj)
    glEnd()

    glBegin(GL_LINE_LOOP)
    for pos, obj in enumerate(verticies):
        if pos <= 14 and pos > 11:
            glVertex3fv(obj)
    glEnd()

    glBegin(GL_LINE_LOOP)
    for pos, obj in enumerate(verticies):
        if pos <= 17 and pos > 14:
            glVertex3fv(obj)
    glEnd()

    glBegin(GL_LINE_LOOP)
    for pos, obj in enumerate(verticies):
        if pos <= 20 and pos > 17:
            glVertex3fv(obj)
    glEnd()

    glBegin(GL_LINE_LOOP)
    for pos, obj in enumerate(verticies):
        if pos <= 23 and pos > 20:
            glVertex3fv(obj)
    glEnd()

    glBegin(GL_LINE_LOOP)
    for pos, obj in enumerate(verticies):
        if pos <= 26 and pos > 23:
            glVertex3fv(obj)
    glEnd()

    glBegin(GL_LINE_LOOP)
    for pos, obj in enumerate(verticies):
        if pos <= 29 and pos > 26:
            glVertex3fv(obj)
    glEnd()

    glColor3f(1,0,0)
    glBegin(GL_LINE_LOOP)
    for pos,obj in enumerate(verticies):
        if pos <= 32 and pos > 29:
            glVertex3fv(obj)
    glEnd()
def main():
    glfw.init()
    window = glfw.create_window(600,600,"window - 02",None,None)
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)
    init()
    while not glfw.window_should_close(window):
        render()
        glfw.poll_events()
        glfw.swap_buffers(window)
    glfw.terminate()
main()