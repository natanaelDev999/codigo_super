import LibraryVectorNatan

vetor = (2,2)
vetor2 = (1,0)

vetor3 = (0,1,1)
vetor4 = (0,1,1)

matriz1 = [[1,0],
           [0,1],
           [1,1]]

# utiliza biblioteca
tamanho = LibraryVectorNatan.tamanho_vetor(vetor)
vetor_normalizado = LibraryVectorNatan.normaliza_vetor(vetor)
soma = LibraryVectorNatan.soma_vetores(vetor,vetor2)
subtracao = LibraryVectorNatan.subtrai_vetores(vetor,vetor2)
produto = LibraryVectorNatan.multiplica_vetores(vetor,vetor2)
quociente = LibraryVectorNatan.divide_vetores(vetor2,vetor)
produto_escalar = LibraryVectorNatan.produto_escalar2(vetor,vetor2)
produto_escalar2 = LibraryVectorNatan.produto_escalar3(vetor3,vetor4)
vetor_mm = LibraryVectorNatan.multiplica_vetor_matriz(vetor,matriz1)
# visualiza
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print(f"soma: {soma}; subtracao: {subtracao};produto: {produto}; quociente: {quociente}; tamanho: {tamanho}; normalização: {vetor_normalizado}; produto escalar: {produto_escalar}")
print(produto_escalar2)
print("resultado da multiplicação vetor e matriz",vetor_mm)

