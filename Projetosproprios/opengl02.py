import glfw
from OpenGL.GL import *

verticies = [[-0.5,-0.5],
             [0.0,0.5],
             [0.5,-0.5]]
cores = [[1,0,0],
         [0,1,0],
         [0,0,1]]

def init():
    glClearColor(1,1,1,1)
def render():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_TRIANGLES)
    for pos,vert in enumerate(verticies):
        glColor3f(cores[pos][0],cores[pos][1],cores[pos][2])
        glVertex2fv(vert)
    glEnd()
def main():
    glfw.init()
    window = glfw.create_window(600,600,"window - 02",None,None)
    glfw.make_context_current(window)
    init()
    while not glfw.window_should_close(window):
        render()
        glfw.poll_events()
        glfw.swap_buffers(window)
    glfw.terminate()
main()