import LibraryRenderNatanT as lvt
import time

codigo_TelShader = '''
p=pr;

mvm 0 vecXY;
'''

matriz_id_0 = [[1,0,0],
               [0,1,0],
               [0,0,1]]

dados_vertices = [[-2,-2,1],[-2,2,1],[2,2,1],
                  [2,-2,1],[-2,-2,1],[2,2,1]]
dados_cores = [[255,0,0],[255,0,0],[255,0,0],
               [255,255,0],[255,255,0],[255,255,0]]

lvt.adiciona_dados("BDV",dados_vertices)
lvt.adiciona_dados("BDA",dados_cores)
lvt.adiciona_dados("BDM",matriz_id_0,0)
lvt.cria_tela(20,20)
while True:
    comeco = time.perf_counter()
    proj = lvt.projeta_vertices(0,False)# 0.000035
    lvt.desenha_triangulo(proj,0,6)# 0.000071
    lvt.compila_codigo_telshader(codigo_TelShader)# 0.000071
    lvt.imprime_tela()# 0.009806
    lvt.trata_terminal(1)# 0.016459
    fim = time.perf_counter()
    #print(f'{fim-comeco:.6f}')