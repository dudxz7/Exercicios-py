import random

class JogoAdivinhacao:
    def __init__(self):
        self.numero_aleatorio = random.randint(1, 100)
        self.tentativas = 0

    def jogar(self):
        print("Bem-vindo ao Jogo de Adivinhação!")
        print("Tente adivinhar o número secreto entre 1 e 100.")

        while True:
            tentativa = int(input("Digite sua tentativa: "))
            self.tentativas += 1

            if tentativa < self.numero_aleatorio:
                print("O número secreto é maior!")
            elif tentativa > self.numero_aleatorio:
                print("O número secreto é menor!")
            else:
                print(f"Parabéns! Você acertou o número secreto {self.numero_aleatorio} em {self.tentativas} tentativas!")
                break

jogo = JogoAdivinhacao()
jogo.jogar()

#aproveitando a tématica, advinha só quem passou por aqui ele mesmo, duduzinreidelas (12/07/2008 odeio essa data tanto que eu nem sei se é 2008 ou 2007 )