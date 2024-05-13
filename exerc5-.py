class conta_bancaria:
    def __init__(self):
        pass
    
    def deposito(self, valor_deposito, saldo):
        return saldo + valor_deposito
    
    def saque(self, valor_saque, saldo, nome):
        if valor_saque > saldo:
            return("O valor excede o limite da conta.")
        else:
            sacar = saldo - valor_saque
            return("Olá", nome, "você sacou", valor_saque, "reais. O saldo atual da sua conta é", sacar, "reais")
    
    def acao(self):
        nome = input("Digite o seu nome: ")
        saldo = float(input("Informe o saldo atual da conta: "))
        acao = input("Você deseja fazer um deposido ou um saque? ")
        if (acao == "deposito"):
            valor_deposito = float(input("Quanto você deseja depositar? "))
            depositado = self.deposito(valor_deposito, saldo)
            print("Olá", nome, "você depositou", valor_deposito, "reais. O saldo atual da sua conta é", depositado, "reais")
        
        elif (acao == "saque"):
            valor_saque = float(input("Quanto você deseja sacar? "))
            sacado = self.saque(valor_saque, saldo, nome)
            print(sacado)
            
banco = conta_bancaria()
banco.acao() 