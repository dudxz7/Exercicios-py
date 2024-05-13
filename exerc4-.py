class calculadora:
    def __init__(self):
        pass
    def soma(self, num1, num2):
        return num1 + num2
    def subtração(self, num1, num2):
        return num1 - num2
    def multiplicação(self, num1, num2):
        return num1 * num2
    def divisão (self, num1, num2):
        if (num2 == 0):
            return "não dá pra dividir por zero né mo fi!"
        else:
            return num1/num2 
    
    def calcular (self):
        operacao = input ("digite a operaqção desejada(+, *, /, -):")
        num1 = float(input("Informe o primeiro número: "))
        num2 = float(input("Informe o segundo número:"))
        if operacao == "+":
            resultado=self.soma(num1,num2)
        elif operacao == "-":
            resultado=self.subtração(num1,num2)
        elif operacao == "*":
            resultado=self.multiplicação(num1,num2)
        elif operacao == "/":
            resultado=self.divisão(num1,num2)
        else:
            print("operação inválida")
        print("resultado:", resultado)
        
minhacalculadora = calculadora()
minhacalculadora.calcular()

