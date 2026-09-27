import LibraryRenderNatanT as lvt
import time

codigo_TelShader = '''
p=█;
ptf c1 0;
3ptf co1;
3ptf color;

mdf co1 0 255;
dva co1 0 c1;
mdf color 1 c1;

cp=color;
'''

dados_vertices = [[0,-2,1],[-2,2,1],[2,2,1]]
dados_cores = [[255,0,0],[255,0,0],[255,0,0]]

lvt.adiciona_dados("BDV",dados_vertices)
lvt.adiciona_dados("BDA",dados_cores)
lvt.cria_tela(20,20)
while True:
    comeco = time.perf_counter()
    proj = lvt.projeta_vertices(0,True)# 0.000035
    lvt.desenha_triangulo(proj,0,3)# 0.000071
    lvt.compila_codigo_telshader(codigo_TelShader)# 0.000071
    lvt.imprime_tela()# 0.009806
    lvt.trata_terminal(1)# 0.016459
    fim = time.perf_counter()
    #print(f'{fim-comeco:.6f}')