from numba import jit
import time

def calcula_soma():
    v = 0
    for c in range(50_000_000):
        v+=1
    return v

comeco = time.perf_counter()
nova_funcao = jit()(calcula_soma)
print(nova_funcao())
fim = time.perf_counter()
print(round(fim- comeco,2))