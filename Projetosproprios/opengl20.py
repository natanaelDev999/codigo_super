# biblioteca para a janela
import glfw
# biblioteca para o desenho
from OpenGL.GL import *
# biblioteca para dados
import numpy as np
# para o uso de ponteiros
import ctypes
# biblioteca para matemática matricial
import pyrr
# biblioteca para matemática básica com ângulos
import math

# variáveis
vao_id = 0
shader_program_id = 0
# endereço de informs
id_uniform_projecao = 0
id_uniform_cor_luz = 0
# camera
camera_alvo = pyrr.Vector3([0.0, 0.0, 0.0])
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
        # posição   \\   cor   \\ normal
        # frente
        [0.2, 0.2, 0, 1, 0, 0, 0, 0, 1],
        [-0.2, 0.2, 0, 1, 0, 0, 0, 0, 1],
        [0.2, -0.2, 0, 1, 0, 0, 0, 0, 1],
        [-0.2, -0.2, 0, 1, 0, 0, 0, 0, 1],
        # atrás
        [0.2, 0.2, 0.36, 1, 0, 0, 0, 0, -1],
        [-0.2, 0.2, 0.36, 1, 0, 0, 0, 0, -1],
        [0.2, -0.2, 0.36, 1, 0, 0, 0, 0, -1],
        [-0.2, -0.2, 0.36, 1, 0, 0, 0, 0, -1]
    ]
faces = [
    # atrás
    [4, 5, 7],
    [4, 6, 7],
    # frente
    [0, 1, 3],
    [0, 2, 3],
    # lado esquerdo
    [0, 4, 6],
    [0, 2, 6],
    # lado direito
    [1, 5, 3],
    [3, 5, 7],
    # cima
    [0, 4, 1],
    [4, 1, 5],
    # baixo
    [2, 6, 3],
    [6, 3, 7],
]
# quantidade de vértices
quantidade_vertices = len(vertices)
# quantidade de faces
quantidade_faces = len(faces)


# função para entrada de teclado
def key_callback(window, key, scancode, action, mods):
    global camera_alvo
    if key == glfw.KEY_W:
        camera_alvo[1] += 0.05
    elif key == glfw.KEY_S:
        camera_alvo[1] -= 0.05
    elif key == glfw.KEY_A:
        camera_alvo[0] -= 0.05
    elif key == glfw.KEY_D:
        camera_alvo[0] += 0.05
# função inicial
def init():
    global vertices, vao_id, shader_program_id, faces, id_uniform_projecao, camera_visao, id_uniform_cor_luz, posicao_camera,matrix_LookAt
    glClearColor(1, 1, 1, 1)

    # ativa z-buffer
    glEnable(GL_DEPTH_TEST)
    # transforma em uma lista de bytes
    vertices = np.array(vertices, np.dtype(np.float32))
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
                          3,  # quantidade de valores do atributo
                          GL_FLOAT,  # tipo dos valores do atributo
                          GL_FALSE,  # se deve ser normalizada a cor
                          9 * 4,  # tamanho do pulo para os próximos valores do atributo
                          ctypes.c_void_p(0))  # começo dos valores
    # descreve os vértices
    glVertexAttribPointer(1,  # código do atributo (cor)
                          3,  # quantidade de valores do atributo
                          GL_FLOAT,  # tipo dos valores do atributo
                          GL_FALSE,  # se deve ser normalizada a cor
                          9 * 4,  # tamanho do pulo para os próximos valores do atributo
                          ctypes.c_void_p(3 * 4))  # começo dos valores
    # descreve os vértices
    glVertexAttribPointer(2,  # código do atributo (normal)
                          3,  # quantidade de valores do atributo
                          GL_FLOAT,  # tipo dos valores do atributo
                          GL_FALSE,  # se deve ser normalizada a cor
                          9 * 4,  # tamanho do pulo para os próximos valores do atributo
                          ctypes.c_void_p(6 * 4))  # começo dos valores
    glEnableVertexAttribArray(0)  # habilita o atributo de posição location (0)
    glEnableVertexAttribArray(1)  # habilita o atributo de cor location (1)
    glEnableVertexAttribArray(2)  # habilita o atributo de cor location (2)
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

    // recebimento e inserimento de valores
    // cria a variável de saída da cor
    out vec4 cor_fragmento;
    // recebe a cor do fragmento
    in vec3 fragmento_cor;

    //  recebe o valor da cor da luz
    in vec3 v_cor_luz;
    //  ajuste para criação de iluminação ambiente
    vec3 ajuste_luz = vec3(0.25,0.25,0.25);
    //  recebe a normal do fragmento
    in vec3 fragmento_normal;
    //  defini origem da luz
    vec3 pos_luz = vec3(0.0, 0.0, -3.0);
    //  recebe a posição do fragmento
    in vec3 fragmento_pos;

    // função inicial
    void main(){
        // comandos e declarações da função inicial
        // CÁLCULOS DE ILUMINAÇÃO


        float constante = 1.0;
        float linear = 0.09;
        float quadratica = 0.032;
        float distancia = length(pos_luz - fragmento_pos);

        float atenuacao = 2.0 / (constante+linear*distancia+quadratica*(distancia*distancia));

        vec3 direcao_luz = normalize(pos_luz-fragmento_pos);
        float delta = max(dot(fragmento_normal, direcao_luz),0.0);
        vec3 iluminacao_difusa = (delta * v_cor_luz);

        iluminacao_difusa *= atenuacao;

        cor_fragmento = vec4(fragmento_cor*iluminacao_difusa,1.0);
    }        
    '''

    shader_vertices = '''

    #version 330 core

    // carrega o atributo de posição
    layout(location = 0) in vec3 atributo_pos;
    // carrega o atributo de cor     
    layout(location = 1) in vec3 atributo_cor; 
    // carrega o atributo de normal
    layout(location = 2) in vec3 atributo_normal;    


    out vec3 fragmento_cor;
    // matriz de projeção
    uniform mat4 matriz;
    // cor da luz
    uniform vec3 cor_luz;
    out vec3 v_cor_luz;
    // normal do vértice
    out vec3 fragmento_normal;
    // direciona a posição do pixel
    out vec3 fragmento_pos;

    // função inicial
    void main(){
        // comandos e declarações da função inicial
        // informa posição do vértice
        gl_Position = matriz*vec4(atributo_pos,1.0);
        // inseri valor ao vetor de saída para cor
        fragmento_cor = vec3(atributo_cor);
        // inseri valor ao vetor de saída para a cor da luz
        v_cor_luz = vec3(cor_luz);
        // inseri valor ao vetor de saída para o vetor normal
        fragmento_normal = vec3(atributo_normal);
        // inseri valor ao vetor de saída para a posição do fragmento
        fragmento_pos = vec3(atributo_pos);
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
    # descobre a localização do uniform dentro de um shader
    id_uniform_projecao = glGetUniformLocation(shader_program_id, 'matriz')
    id_uniform_cor_luz = glGetUniformLocation(shader_program_id, 'cor_luz')
    # trata matrix de visão

# função para desenho
def render():
    global vao_id, quantidade_vertices, shader_program_id, quantidade_faces,id_uniform_cor_luz,camera_alvo
    # limpa a tela utilizando junto, o z-buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # ATIVA
    # ativa os shader
    glUseProgram(shader_program_id)
    ########
    # cálculo matricial para renderização 3D

    aspect_ratio = 600 / 600
    # matrizes
    projecao = pyrr.matrix44.create_perspective_projection_matrix(45.0, aspect_ratio, 0.1, 100.0)
    # multiplição de matrizes
    # camera
    camera_visao = None
    posicao_camera = pyrr.Vector3([0.0, 0.0, 3])
    vetor_cima = pyrr.Vector3([0.0, 1.0, 0.0])
    # matriz
    # | right.x   right.y   right.z   -dot(right, eye)   |
    # | up.x      up.y      up.z      -dot(up, eye)      |
    # | dir.x     dir.y     dir.z     -dot(dir, eye)     |
    # | 0         0         0         1                   |
    matrix_LookAt = pyrr.matrix44.create_look_at(
        eye=posicao_camera,
        target=camera_alvo,
        up=vetor_cima
    )
    camera_visao = matrix_LookAt
    matrix_completa_projecao = pyrr.matrix44.multiply(camera_visao, projecao)

    ########
    # deixa o vao ativo
    glBindVertexArray(vao_id)
    # desenha
    # dar valor aos uniforms
    # manda informação para o uniform
    glUniformMatrix4fv(id_uniform_projecao,  # local do uniform
                       1,  # quantidade de valores a serem inseridos
                       GL_FALSE,  # se deve haver transposição
                       matrix_completa_projecao  # dado a ser inserido no uniform
                       )
    glUniform3f(id_uniform_cor_luz, 1.0, 1.0, 1.0)

    # desenho indexado
    glDrawElements(GL_TRIANGLES,  # modo de desenho
                   3 * quantidade_faces,  # onde deve terminar
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
    window = glfw.create_window(600, 600, "OpenGL moderno 3D", None, None)
    # faz entrada de teclado
    glfw.set_key_callback(window, key_callback)
    # utiliza o contexto opengl
    glfw.make_context_current(window)
    # limita o fps
    glfw.swap_interval(1)
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