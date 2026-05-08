import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders as ops
import numpy as np
import ctypes as ct
shaderid = 0
verticies = [[-0.05,0.0, 0,1,0],[0.05,0.0, 0,1,0],[-0.0,0.8, 0,1,0]
            ]
vaoid = 0
def key_callback(window, key, scancode, action, mods):
    global verticies
    if key == glfw.KEY_A and action == glfw.PRESS:
        for vert in verticies:
            vert[1] -= 0.05
    elif key == glfw.KEY_D and action == glfw.PRESS:
        for vert in verticies:
            vert[1] += 0.05
def init():
    global verticies
    global vaoid,shaderid
    glClearColor(0,0,0,0)
    verticies = np.array(verticies,np.dtype(np.float32))
    vaoid = glGenVertexArrays(1)
    glBindVertexArray(vaoid)
    #criar vbo
    vboid = glGenBuffers(1)
    #fazer o vbo ficar ativo
    glBindBuffer(GL_ARRAY_BUFFER,vboid)
    #enviar os dados a vbo
    glBufferData(GL_ARRAY_BUFFER,verticies.nbytes,verticies,GL_STATIC_DRAW)
    glVertexAttribPointer(0,2,GL_FLOAT,GL_FALSE,5*4,ct.c_void_p(0))

    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 5 * 4, ct.c_void_p(2*4))

    glEnableVertexAttribArray(0)
    glEnableVertexAttribArray(1)

    glBindBuffer(GL_ARRAY_BUFFER,0)
    glBindVertexArray(0)
    #criar shader
    #código-fonte dos shaders
    #ler os arquivos
    with open('vertex.glsl','r') as vt:
        vt_ = vt.read()

    with open('fragment.glsl','r') as fg:
        fg_ = fg.read()
    #criar objeto , trata e compila
    vs = ops.compileShader(vt_,GL_VERTEX_SHADER)
    # vs = glCreateShader(GL_VERTEX_SHADER)
    # glShaderSource(vs,vt_)
    # glCompileShader(vs)
    # if not glGetShaderiv(vs, GL_COMPILE_STATUS):
    #     rsp = glGetShaderInfoLog(vs)
    #     print(rsp)

    fg2 = ops.compileShader(fg_, GL_FRAGMENT_SHADER)
    shaderid = ops.compileProgram(vs,fg2)
    # fg2 = glCreateShader(GL_FRAGMENT_SHADER)
    # glShaderSource(fg2,fg_)
    # glCompileShader(fg2)
    # if not glGetShaderiv(fg2, GL_COMPILE_STATUS):
    #     rsp = glGetShaderInfoLog(fg2)
    #     print(rsp)

    # #criar um shader program
    # sid = glCreateProgram()
    # glAttachShader(sid,vs)
    # glAttachShader(sid, fg2)
    # glLinkProgram(sid)
def render():
    glClear(GL_COLOR_BUFFER_BIT)
    glUseProgram(shaderid)
    glBindVertexArray(vaoid)
    glDrawArrays(GL_TRIANGLES,0,len(verticies))
    glBindVertexArray(0)
    glUseProgram(0)

def main():
    glfw.init()
    window = glfw.create_window(600,600,"window - vbo - vao - shades",None,None)
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)
    init()
    while not glfw.window_should_close(window):
        render()
        glfw.poll_events()
        glfw.swap_buffers(window)
    glfw.terminate()
main()