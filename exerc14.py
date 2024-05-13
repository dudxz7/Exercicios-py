import random

class Dado:
    def __init__(self, lados):
        self.lados = lados

    def lancar_dado(self):
        return random.randint(1, self.lados)


def jogar_dado_personalizado():
    num_lados = int(input("Quantos lados o seu dado terá? "))
    dado_personalizado = Dado(num_lados)
    resultado_personalizado = dado_personalizado.lancar_dado()
    print(f"O seu dado com {num_lados} lados foi lançado e o número que caiu foi: {resultado_personalizado}")


d4 = Dado(4)
d6 = Dado(6)
d8 = Dado(8)
d10 = Dado(10)
d12 = Dado(12)
d20 = Dado(20)


def jogar_dados_padrao():
    print("Sorteio dos dados padrão:")
    print("Resultado do lançamento do D4:", d4.lancar_dado())
    print("Resultado do lançamento do D6:", d6.lancar_dado())
    print("Resultado do lançamento do D8:", d8.lancar_dado())
    print("Resultado do lançamento do D10:", d10.lancar_dado())
    print("Resultado do lançamento do D12:", d12.lancar_dado())
    print("Resultado do lançamento do D20:", d20.lancar_dado())


jogar_dado_personalizado()
jogar_dados_padrao()