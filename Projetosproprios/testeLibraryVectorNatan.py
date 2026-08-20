import LibraryVectorNatan

vetor = (2,1)
vetor2 = (1,0)

tamanho = LibraryVectorNatan.tamanho_vetor(vetor)# 0.000015
vetor_normalizado = LibraryVectorNatan.normaliza_vetor(vetor)
soma = LibraryVectorNatan.soma_vetores(vetor,vetor2)
subtracao = LibraryVectorNatan.subtrai_vetores(vetor,vetor2)
produto = LibraryVectorNatan.multiplica_vetores(vetor,vetor2)
quociente = LibraryVectorNatan.divide_vetores(vetor2,vetor)
print(soma)
print(subtracao)
print(produto)
print(quociente)
print(tamanho)
print(vetor_normalizado)

