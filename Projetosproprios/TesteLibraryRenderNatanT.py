import LibraryRenderNatanT as lvt
import time

dados_vertices = [[0,0,1],[-2,2,1],[2,2,1],
                  [0,0,1.5],[-2,2,1.5],[2,2,1.5]]
dados_cores = [[255,0,0],[255,0,0],[255,0,0],[0,0,255],[0,0,255],[0,0,255]]

lvt.adiciona_dados("BDV",dados_vertices)
lvt.adiciona_dados("BDA",dados_cores)
lvt.cria_tela(10,10)
while True:
    comeco = time.perf_counter()
    proj = lvt.projeta_vertices()
    #lvt.desenha_linhas(proj)
    lvt.desenha_triangulo(proj,0,3,[255,0,0])
    lvt.desenha_triangulo(proj,3,6,[0,0,255])
    # lvt.desenha_triangulo(proj,3,6,[255,0,0])
    lvt.imprime_tela()
    lvt.trata_terminal()
    fim = time.perf_counter()
    print(f'{fim-comeco:.6f}')