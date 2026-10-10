import LibraryRenderNatanT as lvt
import time

codigo_TelShader = '''
p=pr;
'''

codigo_TelTShader = '''
p=.;
3ptf cor;
case x % 2;
$p=*;
$cp=155,155,0;
ec;
case x %? 2;
$cp=155,0,155;
ec;
case y % 2;
$p=*;
$cp=155,155,0;
ec;
case y %? 2;
$cp=155,0,155;
ec;
'''

codigo_tms = '''
ful vecO vecI;
ptf t1 1;
ptf t2 10;
loc t1 t2*10;
mulm 0 vecO;
'''

matriz_id_0 = [
               [1,0,0],
               [0,1,0],
               [0,0,1]
              ]
'''

 'Anatomia' de uma matriz
         eX dX tx
         dY eY ty 
         0  0  eZ
         
 'e' é escala
 't' é translação 
 'd' é distorção adiagonal 
'''

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
    lvt.compila_codigo_TelMatrixShader(codigo_tms)# 0.000118
    proj = lvt.projeta_vertices(0,False)# 0.000035
    lvt.desenha_triangulo(proj,0,6)# 0.000071
    lvt.compila_codigo_TelShader(codigo_TelShader)# 0.000071
    lvt.compila_codigo_TelTShader(codigo_TelTShader)
    lvt.imprime_tela()# 0.009806
    lvt.trata_terminal(1)# 0.016459
    lvt.preserva_dados()
    fim = time.perf_counter()
    print(f'{fim-comeco:.6f}')