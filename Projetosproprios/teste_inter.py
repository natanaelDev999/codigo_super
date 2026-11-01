import time
a = [10,20]
comeco = time.perf_counter()
interator = iter(a)
fim = time.perf_counter()
print(f"tempo :{fim - comeco:.9f}")