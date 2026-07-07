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
# vertices
vertices = [[0,0.2],
             [-0.2,-0.2],
             [0.2,-0.2]]
# quantidade de vértices
quantidade_vertices = len(vertices)
# função inicial
def init():
    global vertices,vao_id,shader_program_id
    glClearColor(1,1,1,1)

    # transforma em uma lista de bytes
    vertices = np.array(vertices,np.dtype(np.float32))# 32 bits
    # VAO
    vao_id = glGenVertexArrays(1)# quantidade de vaos
    # tornar o vao ativo
    glBindVertexArray(vao_id)
    # VBO
    # criar o vbo
    vbo_id = glGenBuffers(1)# quantidade de vbos
    # tornar o vbo ativo
    glBindBuffer(GL_ARRAY_BUFFER,vbo_id)
    # enviar dados para vbo
    glBufferData(GL_ARRAY_BUFFER, # tipo de buffer
                 vertices.nbytes, # quantidade de bytes do buffer
                 vertices, # dados
                 GL_STATIC_DRAW) # o uso do buffer
    # descreve os vértices
    glVertexAttribPointer(0, # código do atributo (posição)
                          2, # quantidade de valores do atributo
                          GL_FLOAT, # tipo dos valores do atributo
                          GL_FALSE, # se deve ser normalizada a cor
                          2*4, # tamanho do pulo para os próximos valores do atributo
                          ctypes.c_void_p(0))
    # torna novamente o vbo ativo
    glEnableVertexAttribArray(0)
    # desetiva o vbo
    glBindBuffer(GL_ARRAY_BUFFER,0)
    # desativa vao
    glBindVertexArray(0)
    # código dos shaders
    # SHADERS

    # criar shaders

    # código-fonte
    #  1-declara a versão de glsl
    #  2-declaração de entrada e saída
    #  3-criação do loop principal
    shader_fragmento = '''
    
    #version 330 core 
    
    out vec4 cor_fragmento;
    
    void main(){
        float cor_refereciada = gl_FragCoord.x / 450.0;
        cor_fragmento = vec4(cor_refereciada,0.0,0.0,1);
    }        
    '''

    shader_vertices = '''
    
    #version 330 core
    
    layout(location = 0) in vec2 atributo_pos;     
            
    void main(){
        gl_Position = vec4(atributo_pos,0.0,1.0);
    }               
    '''

    # criar objeto vertex shader
    vertex_id = glCreateShader(GL_VERTEX_SHADER) # id do shader
    # enviar o código-fonte do shader
    glShaderSource(vertex_id,shader_vertices) # utiliza o id para enviar o shader
    # compilar o vertex shader
    glCompileShader(vertex_id) # compila o código-fonte do shader
    # vereficar se existe um erro
    if not glGetShaderiv(vertex_id,GL_COMPILE_STATUS):
        # se houver erro o imprime na tela
        info = glGetShaderInfoLog(vertex_id)
        print(info)

    # criar objeto fragment shader
    fragment_id = glCreateShader(GL_FRAGMENT_SHADER) # id do shader
    # enviar o código-fonte do shader
    glShaderSource(fragment_id, shader_fragmento)  # utiliza o id para enviar o shader
    # compilar o fragment shader
    glCompileShader(fragment_id) # compila o código-fonte do shader
    # vereficar se existe um erro
    if not glGetShaderiv(fragment_id,GL_COMPILE_STATUS):
        # se houver erro o imprime na tela
        info = glGetShaderInfoLog(fragment_id)
        print(info)

    # unir os shader
    # criar shader program
    shader_program_id = glCreateProgram()
    # associa shaders
    glAttachShader(shader_program_id,vertex_id)
    glAttachShader(shader_program_id,fragment_id)
    # 'linka' os shader
    glLinkProgram(shader_program_id)

# função para desenho
def render():
    global vao_id,quantidade_vertices,shader_program_id
    glClear(GL_COLOR_BUFFER_BIT)
    # ATIVA
    # ativa os shader
    glUseProgram(shader_program_id)
    # deixa o vao ativo
    glBindVertexArray(vao_id)
    # desenha
    glDrawArrays(GL_TRIANGLES,# modo de desenho
                 0,# onde deve começar
                 quantidade_vertices# onde deve terminer
                 )
    # DESATIVA
    # desativa o vao
    glBindVertexArray(0)
    # desativa shaders
    glUseProgram(0)
# função central
def main():
    # cria janela
    glfw.init()
    window = glfw.create_window(600,600,"vbo - vao",None,None)
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