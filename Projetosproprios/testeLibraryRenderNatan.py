import libraryRenderNatan
import time
import math
# Inicialização
# Armazena, transforma e cria dados
# Cria dados
'''
   cubo
[-2.5,2,1],
[2.5,2,1],
[2.5,-2,1],
[-2.5,-2,1],

[-2.5,2,1],
[-2.5,-2,1],
[2.5,2,1],
[2.5,-2,1],


[-2.5,2,2],
[2.5,2,2],
[2.5,-2,2],
[-2.5,-2,2],

[-2.5,2,2],
[-2.5,-2,2],
[2.5,2,2],
[2.5,-2,2],


[-2.5,2,1],
[-2.5,2,2],
[2.5,2,1],
[2.5,2,2],
[2.5,-2,1],
[2.5,-2,2],
[-2.5,-2,1],
[-2.5,-2,2]'''
buffer_de_desenho = [
[-4,4,1,True],
[4,4,1,True],
[4,4,1,True],
[0,0,1,True],
[0,0,1,True],
[-4,4,1,True]
]
codigo_lsln = '''
pr=p;
//t vecto 2 1;
//MMV 1 vecto;
//cs x = 9 ;
//$tp xy vecto;
//ec;
'''
codigo_ltln = '''
pr=*;
cs x %2 2 ;
$cp=34;
ec;
cs x %+ 2 ;
$cp=32;
ec;
'''
codigo_lmln = '''
t vetor 4 0 0 ;
MMV 2 v3;
ts v3 vetor;
'''
matriz_id_1 = [[2,0],
               [0,2]]
ang = 5
angulo = math.radians(ang)
matriz_id_2 = [[math.cos(angulo),-math.sin(angulo),0],
               [math.sin(angulo),math.cos(angulo),0],
               [0,0,1]]
'''matriz_id_2 = [[1,0,0],
               [0,1,0],
               [0,0,1]]'''
#  Transforma dados
cores_pontos = libraryRenderNatan.converte_RGB_ANSI([[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0]])# 0.000013
cor_linha = libraryRenderNatan.converte_RGB_ANSI([[1,1,0]])# 0.000008
cores_preenche = libraryRenderNatan.converte_RGB_ANSI([[1,0,0],[1,1,0]])# 0.000008
# Manda dados para o centro de processamento da libraryRenderNatan
libraryRenderNatan.adiciona_dados('BDV',buffer_de_desenho)# 0.000013
libraryRenderNatan.adiciona_dados('BDA',cores_pontos)# 0.000008
libraryRenderNatan.adiciona_dados('BDM',matriz_id_1,1)# 0.000009
libraryRenderNatan.adiciona_dados('BDM',matriz_id_2,2)# 0.000012
libraryRenderNatan.cria_tela(16, 18)# 0.000063
libraryRenderNatan.utiliza_codigo_LMLN(codigo_lmln)# 0.000116
# Loop principal
# Utiliza os dados da inicialização para renderização
while True:
    comeco = time.perf_counter()
    buffer = libraryRenderNatan.projeta_vertices()# 0.000089
    buffer_pixels_linha = libraryRenderNatan.desenha_linhas(buffer, 0, 40, cor_linha)# 0.000046
    libraryRenderNatan.preenche_forma(buffer_pixels_linha, cores_preenche)# 0.000516
    tela = libraryRenderNatan.desenha_pontos(buffer)# 0.000062
    libraryRenderNatan.utiliza_codigo_LSLN(codigo_lsln)# 0.000384
    libraryRenderNatan.utiliza_codigo_LTLN(codigo_ltln)# 0.000723
    print(36*'-')
    libraryRenderNatan.desenha_tela(tela)# print() -> 0.029529; sys.stdout.write() -> 0.016820 ; Δ = 0.012709
    print(36 * '-')
    libraryRenderNatan.trata_terminal(6)# 0.016236
    fim = time.perf_counter()
    print(f'{fim-comeco:.6f}\n')