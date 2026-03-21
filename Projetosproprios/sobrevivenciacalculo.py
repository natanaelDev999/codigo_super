def desenhar():
    print('-'*30)

class Animal:
    def __init__(self, nome):
        self.nome = nome
        self.vel_a = 0   # tempo do animal
        self.vel_p = 0   # tempo do predador
        self.dis_a = 0   # distância do animal
        self.dis_p = 0   # distância do predador
        self.chance = 50 # chance inicial

    def coleta_de_dados(self):
        desenhar()
        self.dis_a = float(input('Qual a distância do animal até o objetivo: '))
        self.vel_a = float(input(f'Quanto tempo leva para o animal correr {self.dis_a:.2f}m: '))
        desenhar()
        self.dis_p = float(input('Qual a distância do predador até o objetivo: '))
        self.vel_p = float(input(f'Quanto tempo leva para o predador correr {self.dis_p:.2f}m: '))
        desenhar()

    def analise_de_dados(self):
        # Comparação de distância
        if self.dis_a < self.dis_p:
            self.chance += 25
        else:
            self.chance -= 25

        # Comparação de tempo (quem chega mais rápido)
        if self.vel_a < self.vel_p:
            self.chance += 25
        else:
            self.chance -= 25
    def saida_de_dados(self):
        print(f'A chance de sucesso é de {self.chance}%')

# Exemplo de uso
animal = Animal('macaco')
animal.coleta_de_dados()
animal.analise_de_dados()
animal.saida_de_dados()
