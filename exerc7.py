import random
import math

class JogoDado:
    def __init__(self):
        pass

    def lançar_dado(self):
        numero = random.randint(1, 6)  
        return numero

    def jogar(self):
        numero_lançado = self.lançar_dado()  
        raiz_quadrada = math.sqrt(numero_lançado) 
        print("Número lançado:", numero_lançado)
        print("A raiz quadrada do número lançado é:", raiz_quadrada)

jogo = JogoDado()
jogo.jogar()

