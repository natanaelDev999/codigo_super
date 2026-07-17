import glfw
from OpenGL.GL import *
def key_callback(window, key, scancode, action, mods):
    if key == glfw.KEY_A and action == glfw.PRESS:
        verticies[0][1] -= 0.01
        verticies[0][0] += 0.01
        #
        verticies2[0][1] += 0.01
        verticies2[1][1] -= 0.01
        verticies2[0][0] += 0.01
        verticies2[1][0] += 0.01
    elif key == glfw.KEY_D and action == glfw.PRESS:
        verticies[2][1] += 0.01
        verticies[2][0] -= 0.01
        verticies[1][1] -= 0.01
        verticies[1][0] -= 0.01
        #
        verticies2[2][1] += 0.01
        verticies2[2][0] -= 0.01

verticies = [[-0.3,-0.3],[0.3,-0.3],[0.3,0.3]]
verticies2 = [[-0.3,0.3],[-0.3,-0.3],[0.3,0.3]]
def render():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_TRIANGLES)
    glColor3f(0,0,1)
    for verticie in verticies:
        glVertex2fv(verticie)
    for verticie2 in verticies2:
        glVertex2fv(verticie2)
    glEnd()

    glColor3f(0,0,0)
    glBegin(GL_LINES)
    for verticie in verticies:
        glVertex2fv(verticie)
    for verticie in verticies2:
        glVertex2fv(verticie)
    glEnd()
def init():
    glClearColor(1, 1, 1,  1)
    glLineWidth(5)
def main():
    glfw.init()
    window = glfw.create_window(600, 600, "window - 04", None, None)
    glfw.make_context_current(window)
    glfw.set_key_callback(window,key_callback)
    init()
    while not glfw.window_should_close(window):
        render()
        glfw.poll_events()
        glfw.swap_buffers(window)
    glfw.terminate()
main()