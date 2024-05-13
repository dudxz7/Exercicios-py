class conta_bancaria:
    def __init__(self):
        self.__saldo = 0
        self.numero_conta = None
    
    def deposito(self, valor_deposito):
        if valor_deposito > 0:
            self.__saldo += valor_deposito
            print("Depósito de R${:.2f} realizado com sucesso.".format(valor_deposito))
        else:
            print("O valor do depósito deve ser maior que zero.")
    
    def saque(self, valor_saque):
        if valor_saque > 0:
            if valor_saque <= self.__saldo:
                self.__saldo -= valor_saque
                print("Saque de R${:.2f} realizado com sucesso.".format(valor_saque))
            else:
                print("Saldo insuficiente para saque.")
        else:
            print("O valor do saque deve ser maior que zero.")
    
    def get_saldo(self):
        return self.__saldo
    
    def acao(self):
        self.numero_conta = input("Digite o número da conta: ")
        saldo_anterior = float(input("Informe o saldo atual da conta: "))
        self.__saldo = saldo_anterior
        acao = input("Você deseja fazer um depósito ou um saque? ").lower()
        if acao == "deposito":
            valor_deposito = float(input("Quanto você deseja depositar? "))
            self.deposito(valor_deposito)
            print("O saldo atual da conta {} é R${:.2f}".format(self.numero_conta, self.get_saldo()))
        elif acao == "saque":
            valor_saque = float(input("Quanto você deseja sacar? "))
            self.saque(valor_saque)
            print("O saldo atual da conta {} é R${:.2f}".format(self.numero_conta, self.get_saldo()))
        else:
            print("Opção inválida.")


banco = conta_bancaria()
banco.acao()