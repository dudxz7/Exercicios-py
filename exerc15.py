import math

class Ponto:
    def __init__(self):
        self.x = float(input("Digite a coordenada do ponto x : "))
        self.y = float(input("Digite a coordenada do ponto y : "))

    def distancia_origem(self):
        distancia = math.sqrt(self.x ** 2 + self.y ** 2)
        return distancia
    
ponto1 = Ponto()
print("A distância do ponto escolhido ao de origem é de:", ponto1.distancia_origem())
