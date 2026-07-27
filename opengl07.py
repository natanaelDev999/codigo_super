import glfw
from OpenGL.GL import *

def key_callback(window, key, scancode, action, mods):
    global verticies

    if key == glfw.KEY_A and action == glfw.PRESS:
        for vert in verticies:
            vert[0] -= 0.05
        for vert in verticies3:
            vert[0] += 0.008

        verticies[1][1] += 0.008
        verticies[0][1] -= 0.0008
        verticies[2][0] -= 0.00071
        verticies[4][1] += 0.00089
        verticies[6][1] += 0.006
        #
        verticies[9][1] += 0.0057
        verticies[10][1] += 0.0076

    elif key == glfw.KEY_D and action == glfw.PRESS:
        for vert in verticies:
            vert[0] += 0.05
        for vert in verticies3:
            vert[0] -= 0.008

        verticies[1][1] -= 0.008
        verticies[0][1] += 0.0008
        verticies[4][1] -= 0.00089
        verticies[6][1] -= 0.006

        if verticies[2][0] < 0.4563899999999999:
            verticies[2][0] += 0.00071
        else:
            verticies[2][0] -= 0.00071
        #
        verticies[7][1] += 0.00000001
        verticies[8][1] += 0.000046
        verticies[9][1] -= 0.0057
        verticies[10][1] -= 0.0076
    elif key == glfw.KEY_W and action == glfw.PRESS:
        for vert in verticies:
            vert[1] += 0.05
        for vert in verticies3:
            vert[1] -= 0.008

        verticies[2][1] += 0.009
        verticies[3][1] += 0.0088
        verticies[5][1] += 0.0088
        #
        verticies[8][1] -= 0.0007
        verticies[10][1] -= 0.0007
    elif key == glfw.KEY_S and action == glfw.PRESS:
        for vert in verticies:
            vert[1] -= 0.05
        for vert in verticies3:
            vert[1] += 0.008

        verticies[3][1] -= 0.0098
        verticies[5][1] -= 0.0098
        verticies[2][1] -= 0.0099
        #
        verticies[8][1] += 0.0007
        verticies[10][1] += 0.0007
verticies = [[-0.16,0.1],[0.16,0.1],[-0.0,0.2],[-0.0,0.2],[-0.06,0.1],[-0.0,0.2],[0.06,0.1],
             [-0.068,0.1],[-0.08,0.19],[0.068,0.1],[0.08,0.19]]

verticies2 = [
    [-1,0.0],
    [1,0.0],
    [0.0,2],
    [0.0,-2]
]

verticies3 = [
    [0.5,0.4],
    [0.6,0.5],
    [0.3,0.2],
    [-0.5,0.58],
    [-0.6,0.6],
    [-0.5,0.184],
    [0.7,-0.37],
    [0.6,-0.47],
    [0.4,-0.29],
    [-0.5,-0.1],
    [-0.6,-0.5],
    [-0.4,-0.6]
]

def render():
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,1)

    for pos, verticie in enumerate(verticies):
        if pos <= 2:
            glVertex2fv(verticie)

    glEnd()

    glLineWidth(1)

    glBegin(GL_LINES)
    glColor3f(1, 0, 0)

    for vert in verticies2:
        glVertex2fv(vert)

    glEnd()

    glLineWidth(3)

    glBegin(GL_POINTS)
    glColor3f(1,1,1)

    for vert in verticies3:
        glVertex2fv(vert)

    glEnd()
    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,1)
    glVertex2fv(verticies[3])
    glVertex2fv(verticies[4])
    glVertex2fv(verticies[5])
    glVertex2fv(verticies[6])
    glEnd()
    glBegin(GL_LINES)
    glColor3f(0,0,1)
    glVertex2fv(verticies[7])
    glVertex2fv(verticies[8])
    glVertex2fv(verticies[9])
    glVertex2fv(verticies[10])
    glEnd()

def init():
    glClearColor(0, 0, 0, 0)
    glLineWidth(3)
    glPointSize(3)

def draw_data():
    global verticies

    for vert in verticies:
        print(vert[0], ' ', vert[1], '/', end=' ')

def main():
    glfw.init()

    window = glfw.create_window(600, 600, "SuperSpace", None, None)

    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)

    init()

    while not glfw.window_should_close(window):
        render()
        glfw.poll_events()
        glfw.swap_buffers(window)

    draw_data()
    glfw.terminate()

main()