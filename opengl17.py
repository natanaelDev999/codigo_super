# biblioteca para a janela
import glfw
# biblioteca para o desenho
from OpenGL.GL import *
# biblioteca para dados
import numpy as np
# para o uso de ponteiros
import ctypes

# variáveis
vao_id = 0
shader_program_id = 0
# para movimentação
movimento_x = 0
movimento_y = 0
#  local dos uniforms
local_uniform_pos = 0
# vertices
# quadrado
# vértices
# [2,2, 1,0,0]
# [-2,2, 1,0,0]
# [2,-2, 1,0,0]
# [-2,-2, 1,0,0]
# faces
# [0,1,3]
# [0,2,3]
vertices = \
    [
        [0.2, 0.2, 1, 0, 0],
        [-0.2, 0.2, 1, 0, 0],
        [0.2, -0.2, 1, 0, 0],
        [-0.2, -0.2, 1, 0, 0]
    ]
faces = [[0, 1, 3],
         [0, 2, 3]]
# quantidade de vértices
quantidade_vertices = len(vertices)
# quantidade de faces
quantidade_faces = len(faces)

# função para entrada de teclado
def key_callback(window, key, scancode, action, mods):
    global movimento_x,movimento_y
    if key == glfw.KEY_W:
        movimento_y += 0.005
    elif key == glfw.KEY_S:
        movimento_y -= 0.005
    elif key == glfw.KEY_A:
        movimento_x -= 0.005
    elif key == glfw.KEY_D:
        movimento_x += 0.005

# função inicial
def init():
    global vertices, vao_id, shader_program_id, faces,local_uniform_pos
    glClearColor(1, 1, 1, 1)

    # transforma em uma lista de bytes
    vertices = np.array(vertices, np.dtype(np.float32))  # 32 bits
    # VAO
    vao_id = glGenVertexArrays(1)  # quantidade de vaos
    # tornar o vao ativo
    glBindVertexArray(vao_id)
    # VBO
    # criar o vbo
    vbo_id = glGenBuffers(1)  # quantidade de vbos
    # tornar o vbo ativo
    glBindBuffer(GL_ARRAY_BUFFER, vbo_id)
    # enviar dados para vbo
    glBufferData(GL_ARRAY_BUFFER,  # tipo de buffer
                 vertices.nbytes,  # quantidade de bytes do buffer
                 vertices,  # dados
                 GL_STATIC_DRAW)  # o uso do buffer
    # descreve os vértices
    glVertexAttribPointer(0,  # código do atributo (posição)
                          2,  # quantidade de valores do atributo
                          GL_FLOAT,  # tipo dos valores do atributo
                          GL_FALSE,  # se deve ser normalizada a cor
                          5 * 4,  # tamanho do pulo para os próximos valores do atributo
                          ctypes.c_void_p(0))  # começo dos valores
    # descreve os vértices
    glVertexAttribPointer(1,  # código do atributo (cor)
                          3,  # quantidade de valores do atributo
                          GL_FLOAT,  # tipo dos valores do atributo
                          GL_FALSE,  # se deve ser normalizada a cor
                          5 * 4,  # tamanho do pulo para os próximos valores do atributo
                          ctypes.c_void_p(2 * 4))  # começo dos valores
    glEnableVertexAttribArray(0)  # habilita o atributo de posição location (0)
    glEnableVertexAttribArray(1)  # habilita o atributo de cor location (1)
    # EBO
    faces = np.array(faces, dtype=np.uint32)
    # cria ebo
    ebo_id = glGenBuffers(1)
    # ativa o ebo
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo_id)
    # enviar dados para o ebo
    glBufferData(GL_ELEMENT_ARRAY_BUFFER,  # tipo do buffer
                 faces.nbytes,  # quantidade de bytes do buffer
                 faces,  # dados
                 GL_STATIC_DRAW)  # o uso do buffer

    # desativa o vbo
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    # desativa vao
    glBindVertexArray(0)
    # desativa ebo
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)
    # SHADERS

    # criar shaders

    # código-fonte
    #  1-declara a versão de glsl
    #  2-declaração de entrada e saída
    #  3-criação do loop principal
    # detalhes
    #  out - saída
    #  in - entrada
    #  o fragment shader não recebe os atributos diretamente, apenas pelo vertex shader
    shader_fragmento = '''

    #version 330 core 

    out vec4 cor_fragmento;
    in vec3 fragmento_cor;

    void main(){
        cor_fragmento = vec4(fragmento_cor,1.0);
    }        
    '''

    shader_vertices = '''

    #version 330 core

    layout(location = 0) in vec2 atributo_pos;     
    layout(location = 1) in vec3 atributo_cor;     
    uniform vec2 pos_sistema;
    
    out vec3 fragmento_cor;

    void main(){
        gl_Position = vec4(atributo_pos+pos_sistema,0.0,1.0);
        fragmento_cor = vec3(atributo_cor);
    }               
    '''

    # criar objeto vertex shader
    vertex_id = glCreateShader(GL_VERTEX_SHADER)  # id do shader
    # enviar o código-fonte do shader
    glShaderSource(vertex_id, shader_vertices)  # utiliza o id para enviar o shader
    # compilar o vertex shader
    glCompileShader(vertex_id)  # compila o código-fonte do shader
    # vereficar se existe um erro
    if not glGetShaderiv(vertex_id, GL_COMPILE_STATUS):
        # se houver erro o imprime na tela
        info = glGetShaderInfoLog(vertex_id)
        print(info)

    # criar objeto fragment shader
    fragment_id = glCreateShader(GL_FRAGMENT_SHADER)  # id do shader
    # enviar o código-fonte do shader
    glShaderSource(fragment_id, shader_fragmento)  # utiliza o id para enviar o shader
    # compilar o fragment shader
    glCompileShader(fragment_id)  # compila o código-fonte do shader
    # vereficar se existe um erro
    if not glGetShaderiv(fragment_id, GL_COMPILE_STATUS):
        # se houver erro o imprime na tela
        info = glGetShaderInfoLog(fragment_id)
        print(info)

    # unir os shader
    # criar shader program
    shader_program_id = glCreateProgram()
    # associa shaders
    glAttachShader(shader_program_id, vertex_id)
    glAttachShader(shader_program_id, fragment_id)
    # 'linka' os shader
    glLinkProgram(shader_program_id)
    local_uniform_pos = glGetUniformLocation(shader_program_id, 'pos_sistema')

# função para desenho
def render():
    global vao_id, quantidade_vertices, shader_program_id, quantidade_faces,local_uniform_pos,movimento_x,movimento_y
    glClear(GL_COLOR_BUFFER_BIT)
    # ATIVA
    # ativa os shader
    glUseProgram(shader_program_id)
    # deixa o vao ativo
    glBindVertexArray(vao_id)
    # desenha
    # dar valor aos uniforms
    # manda informação para o uniform
    glUniform2f(local_uniform_pos,  # local do uniform
                movimento_x,movimento_y  # código RGB
                )

    # desenho indexado
    glDrawElements(GL_TRIANGLES,  # modo de desenho
                   3 * quantidade_faces,  # onde deve terminer
                   GL_UNSIGNED_INT,  # tipo de dados nos índices
                   None  # onde deve começar
                   )

    # desenho não indexado
    # glDrawArrays(GL_TRIANGLES,# modo de desenho
    #              0,# onde deve começar
    #              quantidade_vertices# onde deve terminer
    #              )

    # DESATIVA
    # desativa o vao
    glBindVertexArray(0)
    # desativa shaders
    glUseProgram(0)


# função central
def main():
    # cria janela
    glfw.init()
    window = glfw.create_window(600, 600, "vbo - vao", None, None)
    # função para entrada de teclado
    glfw.set_key_callback(window, key_callback)
    glfw.make_context_current(window)
    # utiliza a função inicial
    init()
    # loop para renderização
    while not glfw.window_should_close(window):
        # renderiza
        render()
        # configurações
        glfw.poll_events()
        glfw.swap_buffers(window)
    # termina janela
    glfw.terminate()


# utiliza função central
main()