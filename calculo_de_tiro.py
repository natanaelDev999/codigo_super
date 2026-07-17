from math import ceil
print('     Calculadora balistica (dados de distancia e movimetação necessarios)')
class Artilharia:
    def __init__(self, nome):
        self.nome = nome
        self.centimetrospre = 0
        self.centimetros = 0
        self.distancia = 0
        self.ditanciarre = 0
        self.vel = 0
        self.cenfren = 0
    def entrada_de_dados(self):
        self.centimetrospre = float(input('quantos centimetros (de mira) é preciso para o tiro alcançar 10 m: '))
        self.distancia = float(input('quantos metros o tiro deve percorrer: '))
        self.vel = float(input('para cada 10 metros que o alvo se movimenta para o lado quantos centimetros ele muda(na visão):'))
        self.vel_a = int(input('qual a velocidade do alvo arredondada para o um numero redondo:'))
    def analise_da_dados(self):
        if self.distancia % 10 == 0:
            self.centimetros = (self.distancia / 10) * self.centimetrospre
        else:
            self.ditanciarre = ceil(self.distancia / 10) * 10
            self.centimetros = (self.ditanciarre / 10) * self.centimetrospre
            if (self.distancia % 10) < 5:
                self.centimetros += self.centimetrospre / 5
            else:
                self.centimetros += self.centimetrospre / 2
        self.cenfren = (self.vel_a / 10) * self.vel
    def saida_de_dados(self):
        print(f'os centimetros necessarios para o tiro voar {self.distancia} m é de {self.centimetros:.2f} cm\na quantidade de centimetros a frente do alvo é de {self.cenfren:.2f}cm')

atilha = Artilharia('p-14')
atilha.entrada_de_dados()
atilha.analise_da_dados()
atilha.saida_de_dados()
