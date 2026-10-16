import psutil

mem_info = psutil.virtual_memory()

print(f"total {mem_info.total / (1024 ** 3):.2f}GB")

print(f'disponível {mem_info.available / (1024 **3):.2f}GB')

print(f'utilizada {mem_info.used / (1024 **3):.2f}GB')
