import LibraryRenderNatanT as lvt
import time

dados_vertices = [[2,0,1],[-2,0,1]]
dados_cores = [[0,0,255],[255,0,0]]

lvt.adiciona_dados("BDV",dados_vertices)
lvt.adiciona_dados("BDA",dados_cores)
lvt.cria_tela(10,10)
while True:
    comeco = time.perf_counter()
    proj = lvt.projeta_vertices()
    lvt.desenha_linhas(proj)
    lvt.imprime_tela()
    lvt.trata_terminal()
    fim = time.perf_counter()
    print(f'{fim-comeco:.6f}')