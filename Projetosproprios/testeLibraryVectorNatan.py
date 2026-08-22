import LibraryVectorNatan

vetor = (2,2)
vetor2 = (1,0)

# utiliza biblioteca
tamanho = LibraryVectorNatan.tamanho_vetor(vetor)
vetor_normalizado = LibraryVectorNatan.normaliza_vetor(vetor)
soma = LibraryVectorNatan.soma_vetores(vetor,vetor2)
subtracao = LibraryVectorNatan.subtrai_vetores(vetor,vetor2)
produto = LibraryVectorNatan.multiplica_vetores(vetor,vetor2)
quociente = LibraryVectorNatan.divide_vetores(vetor2,vetor)
produto_escalar = LibraryVectorNatan.produto_escalar(vetor,vetor2)
# visualiza
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print(f"soma: {soma}; subtracao: {subtracao};produto: {produto}; quociente: {quociente}; tamanho: {tamanho}; normalização: {vetor_normalizado}; produto escalar: {produto_escalar}")

