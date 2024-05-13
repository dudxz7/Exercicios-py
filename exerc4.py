import math

class calculadora:
    def __init__(self):
        pass

    def soma(self, num1, num2):
        return num1 + num2

    def subtração(self, num1, num2):
        return num1 - num2

    def multiplicação(self, num1, num2):
        return num1 * num2

    def divisão(self, num1, num2):
        if num2 == 0:
            return "não dá pra dividir por zero né mo fi!"
        else:
            return num1 / num2

    def raiz_quadrada(self, num):
        if num >= 0:
            return math.sqrt(num)
        else:
            return "Acho que não existe raiz de 0, ou de número negativo né paizão, só acho rs"

    def calcular(self):
        operacao = input("Digite a operação desejada (+, *, /, -, √): ")

        if operacao in ["+", "-", "*", "/"]:
            num1 = float(input("Informe o primeiro número: "))
            num2 = float(input("Informe o segundo número: "))
            if operacao == "+":
                resultado = self.soma(num1, num2)
            elif operacao == "-":
                resultado = self.subtração(num1, num2)
            elif operacao == "*":
                resultado = self.multiplicação(num1, num2)
            elif operacao == "/":
                resultado = self.divisão(num1, num2)
        elif operacao == "√":
            num = float(input("Informe o número: "))
            resultado = self.raiz_quadrada(num)
        else:
            resultado = "Operação inválida"

        print("A raiz do número escolhido  é:", resultado)

minhacalculadora = calculadora()
minhacalculadora.calcular()