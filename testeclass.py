class Coelhinho:
    def __init__(self,cor,tamanho, nome, idade):
        self.cor = cor
        self.tamanho = tamanho
        self.nome = nome
        self.idade = idade
    def pular(self):
        print(f'{self.nome} pulou')
    def correr(self):
        print(f'{self.nome}esta correndo')

coelho_1 = Coelhinho('branco','grande','mimin', 4)
coelho_2 = Coelhinho('marron','pequeno', 'laura', 7)
print('nome:',coelho_1.nome)
print('cor:',coelho_1.cor)
print('tamanho:', coelho_1.tamanho)
for c in range(1,4):
    coelho_1.pular()
    coelho_1.correr()
def soma(numero):
    numero += 1
def mostra(numero2):
    print(numero2)