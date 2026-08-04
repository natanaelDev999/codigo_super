import libraryRenderNatan
import time
import psutil
import os
buffer_de_desenho = [
 [-3,3,1],
 [3,3,1],
 [3,3,1],
 [0,0,1],
 [0,0,1],
 [-3,3,1]
]
codigo_lsln = '''
pr=p;
t vecto 2 1;
MMV 1 vecto;
cs x = 9 ;
$tp xy vecto;
ec;
'''
libraryRenderNatan.adiciona_dados('BDV',buffer_de_desenho)# 0.000013
libraryRenderNatan.adiciona_dados('BDA',[31,31,31,31,31,31])# 0.000008
libraryRenderNatan.adiciona_dados('BDM',[[2,0],[0,2]],1)# 0.000009
libraryRenderNatan.cria_tela(16, 18)# 0.000063
while True:
    buffer = libraryRenderNatan.projeta_vertices()# 0.000089
    buffer_pixels_linha = libraryRenderNatan.desenha_linhas(buffer, 0, 6, 33)# 0.000046
    libraryRenderNatan.preenche_forma(buffer_pixels_linha, 31, 33)# 0.000516
    tela = libraryRenderNatan.desenha_pontos(buffer)# 0.000062
    libraryRenderNatan.utiliza_codigo_LSLN(codigo_lsln)# 0.000384
    print(36*'-')
    comeco = time.perf_counter()
    libraryRenderNatan.desenha_tela(tela)# print() -> 0.029529; sys.stdout.write() -> 0.016820 ; Δ = 0.012709
    fim = time.perf_counter()
    print(36 * '-')
    libraryRenderNatan.trata_terminal(2)# 0.016236
    print(f'{fim-comeco:.6f}\n')
    processo = psutil.Process(os.getpid())
    print(processo.memory_info().rss / 1024 / 1024, "MB")