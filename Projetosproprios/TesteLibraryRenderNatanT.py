import LibraryRenderNatanT as lvt
import time

codigo_TelShader = '''
p=pr;

mvm 0 vecXY;
'''

codigo_TelTShader = '''
p=.;
3ptf cor;
case x % 2;
$cp=255,255,0;
ec;
case x %? 2;
$cp=255,0,255;
ec;
'''

codigo_tms = '''
ful vecO vecI;
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
lvt.cria_tela(20,40)
while True:
    comeco = time.perf_counter()
    lvt.compila_codigo_TelMatrixShader(codigo_tms)
    proj = lvt.projeta_vertices(0,False)# 0.000035
    lvt.desenha_triangulo(proj,0,6)# 0.000071
    lvt.compila_codigo_TelShader(codigo_TelShader)# 0.000071
    lvt.compila_codigo_TelTShader(codigo_TelTShader)
    lvt.imprime_tela()# 0.009806
    lvt.trata_terminal(1)# 0.016459
    fim = time.perf_counter()
    print(f'{fim-comeco:.6f}')